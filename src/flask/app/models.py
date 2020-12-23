from .globals import db
from sqlalchemy import Column, String, Float, BigInteger, Integer, DateTime
from hashlib import md5
import datetime


class User(db.Model):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  phone = Column(String(11))

  lastname = Column(String(255), nullable=False)
  firstname = Column(String(255), nullable=False)
  middlename = Column(String(255), nullable=False)
  position = Column(String(255))

  email = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)

  def __init__(self, lastname, firstname, middlename, position, phone, email, password, salt):
    self.setLastname(lastname)
    self.setFirstname(firstname)
    self.setMiddlename(middlename)
    self.setPosition(position)
    self.setPhone(phone)
    self.setEmail(email)
    self.setPassword(password, salt)


  def setPosition(self, position):
    position = position.strip() if position else None
    self.position = position

  def setEmail(self, email):
    email = email.strip() if email else ""
    self.email = email

  def setPhone(self, phone):
    phone = phone.strip() if phone else None
    self.phone = phone

  def setLastname(self, lastname):
    self.lastname = lastname.strip()

  def setFirstname(self, firstname):
    self.firstname = firstname.strip()

  def setMiddlename(self, middlename):
    self.middlename = middlename.strip()

  def setPassword(self, password, salt):
    f1 = md5(password.encode("utf8")).hexdigest() + salt
    self.password = md5(f1.encode("utf8")).hexdigest()

class QueryType(db.Model):
  __tablename__ = "query_type"
  id = Column(Integer, primary_key=True)
  name = Column(String(20), nullable=False)

class Unit(db.Model):
  __tablename__ = "units"
  id = Column(Integer, primary_key=True)
  name = Column(String(10), nullable=False)

class Aggregation(db.Model):
  __tablename__ = "aggregations"
  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)


class FkkoClass(db.Model):
  __tablename__ = "fkkoclass"
  id = Column(Integer, primary_key=True)
  name = Column(String(600), nullable=False)


class Fkko(db.Model):
  __tablename__ = "fkko"
  id = Column(BigInteger, primary_key=True)
  parent_id = Column(BigInteger)
  name = Column(String(600), nullable=False)

  fkkoclass_id = Column("fkkoclass_id", Integer, db.ForeignKey('fkkoclass.id'))
  fkkoclass = db.relationship("FkkoClass")

  aggr_id = Column("aggr_id", Integer, db.ForeignKey('aggregations.id'))
  aggr = db.relationship("Aggregation")

class Queries(db.Model):
  __tablename__ = "queries"
  id = Column(Integer, primary_key=True)

  fkko_id = Column("fkko_id", BigInteger, db.ForeignKey('fkko.id'))
  fkko = db.relationship("Fkko")

  waste = Column(String(255))
  region = Column(String(255))
  locality = Column(String(255))
  count = Column(Float)
  date_expiry = Column(DateTime, default=datetime.datetime.utcnow)

  unit_id = Column("unit_id", Integer, db.ForeignKey('units.id'))
  unit = db.relationship("Unit")

  aggr_id = Column("aggr_id", Integer, db.ForeignKey('aggregations.id'))
  aggr = db.relationship("Aggregation")

  user_id = Column("user_id", Integer, db.ForeignKey('users.id'))
  user = db.relationship("User")

  query_type_id = Column("query_type_id", Integer, db.ForeignKey('query_type.id'))
  query_type = db.relationship("QueryType")
