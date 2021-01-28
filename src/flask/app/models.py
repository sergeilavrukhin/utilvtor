from .globals import db
from sqlalchemy import Column, String, Float, BigInteger, Integer, DateTime
from hashlib import md5
import datetime

class Region(db.Model):
  __tablename__ = "regions"
  id = Column(Integer, primary_key=True)
  text = Column(String(255))
  url = Column(String(255))

class User(db.Model):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  phone = Column(String(11))

  lastname = Column(String(255), nullable=False)
  firstname = Column(String(255), nullable=False)
  middlename = Column(String(255), nullable=False)
  position = Column(String(255))
  itn = Column(String(12))

  email = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)

  def __init__(self, lastname, firstname, middlename, position, phone, email, itn, password, salt):
    self.setLastname(lastname)
    self.setFirstname(firstname)
    self.setMiddlename(middlename)
    self.setPosition(position)
    self.setPhone(phone)
    self.setEmail(email)
    self.setITN(itn)
    self.setPassword(password, salt)


  def setPosition(self, position):
    position = position.strip() if position else None
    self.position = position

  def setEmail(self, email):
    email = email.strip() if email else ""
    self.email = email

  def setITN(self, itn):
    itn = itn.strip() if itn else ""
    self.itn = itn

  def setPhone(self, phone):
    phone = phone.strip() if phone else None
    self.phone = phone

  def setLastname(self, lastname):
    self.lastname = lastname.strip()

  def setFirstname(self, firstname):
    self.firstname = firstname.strip()

  def setMiddlename(self, middlename):
    self.middlename = middlename.strip()

  def generateHash(password, salt):
    f1 = md5(password.encode("utf8")).hexdigest() + salt
    return md5(f1.encode("utf8")).hexdigest()

  def setPassword(self, password, salt):
    f1 = md5(password.encode("utf8")).hexdigest() + salt
    self.password = md5(f1.encode("utf8")).hexdigest()


class QueryType(db.Model):
  __tablename__ = "query_type"
  id = Column(Integer, primary_key=True)
  text = Column(String(20), nullable=False)

class Unit(db.Model):
  __tablename__ = "units"
  id = Column(Integer, primary_key=True)
  text = Column(String(10), nullable=False)

class Aggregation(db.Model):
  __tablename__ = "aggregations"
  id = Column(Integer, primary_key=True)
  text = Column(String(255), nullable=False)


class FkkoClass(db.Model):
  __tablename__ = "fkkoclass"
  id = Column(Integer, primary_key=True)
  text = Column(String(600), nullable=False)


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
  moderation = Column(Integer)

  fkko_id = Column("fkko_id", BigInteger, db.ForeignKey('fkko.id'))
  fkko = db.relationship("Fkko")

  waste = Column(String(255))
  region_id = Column("region_id", Integer, db.ForeignKey('regions.id'))
  region = db.relationship("Region")
  locality = Column(String(255))
  count = Column(Float)
  date_create = Column(DateTime, default=datetime.datetime.utcnow)
  date_expiry = Column(DateTime, default=datetime.datetime.utcnow)

  unit_id = Column("unit_id", Integer, db.ForeignKey('units.id'))
  unit = db.relationship("Unit")

  aggr_id = Column("aggr_id", Integer, db.ForeignKey('aggregations.id'))
  aggr = db.relationship("Aggregation")

  user_id = Column("user_id", Integer, db.ForeignKey('users.id'))
  user = db.relationship("User")

  query_type_id = Column("query_type_id", Integer, db.ForeignKey('query_type.id'))
  query_type = db.relationship("QueryType")


  def __init__(self, fkko, unit, aggr, user, query_type, region, waste, count, locality, date_expiry):
    self.setFkko(fkko)
    self.setUnit(unit)
    self.setAggr(aggr)
    self.setUser(user)
    self.setQueryType(query_type)
    self.setRegion(region)
    self.setWaste(waste)
    self.setCount(count)
    self.setLocality(locality)
    self.setDateExpiry(date_expiry)

  def setFkko(self, fkko):
      self.fkko = fkko

  def setUnit(self, unit):
      if not isinstance(unit, Unit):
          raise DomainException("Передан не Ед. Изм")
      self.unit = unit

  def setAggr(self, aggr):
    self.aggr = aggr

  def setUser(self, user):
    if not isinstance(user, User):
      raise DomainException("Передан не пользователь")
    self.user = user

  def setQueryType(self, query_type):
    if not isinstance(query_type, QueryType):
      raise DomainException("Передан не тип запроса")
    self.query_type = query_type

  def setRegion(self, region):
    if not isinstance(region, Region):
      raise DomainException("Передан не регион")
    self.region = region

  def setWaste(self, waste):
    waste = waste.strip() if waste else None
    self.waste = waste

  def setCount(self, count):
    count = count.strip() if count else None
    self.count = count

  def setLocality(self, locality):
    locality = locality.strip() if locality else ""
    self.locality = locality

  def setDateExpiry(self, date_expiry):
    if date_expiry != 0:
      self.date_expiry = date_expiry


class Companies(db.Model):
  __tablename__ = "companies"
  id = Column(Integer, primary_key=True)

  name = Column(String(255))
  itn = Column(String(12))
  # широта
  latitude = Column(String(20), nullable=True)
  # долгота
  longitude = Column(String(20), nullable=True)

  region_id = Column("region_id", Integer, db.ForeignKey('regions.id'))
  region = db.relationship("Region")

  phones = Column(String(600))
  emails = Column(String(600))
  site = Column(String(255))
  activity = Column(String(600))
  locality = Column(String(600))
  gps = Column(String(255))

  def setCoordinates(self, latitude, longitude):
    if latitude.strip() == '':
      latitude = "0.0"
    if longitude.strip() == '':
      longitude = "0.0"
    self.latitude = latitude.strip()
    self.longitude = longitude.strip()