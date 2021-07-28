from .globals import db
from sqlalchemy import Column, String, Float, BigInteger, Integer, DateTime, Text, Boolean
from hashlib import md5
import datetime

class Region(db.Model):
  __tablename__ = "regions"
  id = Column(Integer, primary_key=True)
  text = Column(String(255))
  url = Column(String(255))
  activity = Column(String(600))

class User(db.Model):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  phone = Column(String(11))
  email = Column(String(255))
  firstname = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)
  date_create = Column(DateTime, default=datetime.datetime.utcnow)

  def __init__(self, firstname, phone, email, password, salt):
    self.setFirstname(firstname)
    self.setPhone(phone)
    self.setEmail(email)
    self.setPassword(password, salt)

  def setPhone(self, phone):
    phone = phone.strip() if phone else None
    self.phone = phone

  def setEmail(self, email):
    email = email.strip() if email else None
    self.email = email

  def setFirstname(self, firstname):
    self.firstname = firstname.strip()

  def generateHash(password, salt):
    f1 = md5(password.encode("utf8")).hexdigest() + salt
    return md5(f1.encode("utf8")).hexdigest()

  def setPassword(self, password, salt):
    f1 = md5(password.encode("utf8")).hexdigest() + salt
    self.password = md5(f1.encode("utf8")).hexdigest()


class QueryType(db.Model):
  __tablename__ = "query_type"
  id = Column(Integer, primary_key=True)
  text = Column(String(40), nullable=False)

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
  keywords = Column(Text)

  fkkoclass_id = Column("fkkoclass_id", Integer, db.ForeignKey('fkkoclass.id'))
  fkkoclass = db.relationship("FkkoClass")

  aggr_id = Column("aggr_id", Integer, db.ForeignKey('aggregations.id'))
  aggr = db.relationship("Aggregation")

class Queries(db.Model):
  __tablename__ = "queries"
  id = Column(Integer, primary_key=True)
  moderation = Column(Integer)
  waste = Column(String(255), nullable=False)
  region_id = Column("region_id", Integer, db.ForeignKey('regions.id'))
  region = db.relationship("Region")
  date_create = Column(DateTime, default=datetime.datetime.utcnow)

  user_id = Column("user_id", Integer, db.ForeignKey('users.id'))
  user = db.relationship("User")

  query_type_id = Column("query_type_id", Integer, db.ForeignKey('query_type.id'))
  query_type = db.relationship("QueryType")

  description = Column(Text)


  def __init__(self, user, query_type, region, waste, description):
    self.setUser(user)
    self.setQueryType(query_type)
    self.setRegion(region)
    self.waste = waste
    self.description = description

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
  checked = Column(Boolean, default=False)

  def setCoordinates(self, latitude, longitude):
    if latitude.strip() == '':
      latitude = "0.0"
    if longitude.strip() == '':
      longitude = "0.0"
    self.latitude = latitude.strip()
    self.longitude = longitude.strip()

class CompaniesWaste(db.Model):
  __tablename__ = "waste_c"
  id = Column(Integer, primary_key=True)
  itn = Column(String(12), index = True)
  activity = Column(String(600))

  fkko_id = Column("fkko_id", BigInteger, db.ForeignKey('fkko.id'))
  fkko = db.relationship("Fkko")

class SiteClick(db.Model):
  __tablename__ = "site_click"
  id = Column(Integer, primary_key=True)
  company_id = Column("companies_id", Integer, db.ForeignKey('companies.id'))
  company = db.relationship("Companies")

  def __init__(self, company):
    self.setCompany(company)

  def setCompany(self, company):
    if not isinstance(company, Companies):
      raise DomainException("Передана не компания")
    self.company = company