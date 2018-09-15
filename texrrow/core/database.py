#!/usr/bin/env python
"""Database module, including the SQLAlchemy database object and DB-related
utilities.
"""
from flask import abort

from .extensions import db


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        # Prevent changing ID of object
        kwargs.pop('id', None)
        for attr, value in kwargs.iteritems():
            # Flask-RESTful makes everything None by default :/
            if value is not None:
                setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True

    def refresh(self, *attribute_names):
        return db.session.refresh(self, attribute_names=attribute_names)

    def __str__(self):
        raise NotImplementedError


# From Mike Bayer's "Building the app" talk
# https://speakerdeck.com/zzzeek/building-the-app
class SurrogatePK(object):
    """A mixin that adds a surrogate integer 'primary key' column named
    ``id`` to any declarative-mapped class.
    """
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def last(cls):
        return cls.query.order_by(cls.id.desc()).first()

    @classmethod
    def get(cls, idx: int):
        return cls.query.get(idx)

    @classmethod
    def get_or_404(cls, idx):
        """
        Returns the account from the ID or username.
        If it fails, a 404 response is made.
        """
        # [1] => username is not None ...
        entry = cls.get(idx)
        if not entry:
            abort(404)
        return entry

    @classmethod
    def filter_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def filtered_first_or_404(cls, **kwargs):
        entry = cls.filter_by(**kwargs).first()
        if not entry:
            abort(404)
        return entry
