CREATE TABLE STAND
(
  id_stand INT NOT NULL,
  stand_name VARCHAR NOT NULL,
  PWR CHAR NOT NULL,
  SPD CHAR NOT NULL,
  RNG CHAR NOT NULL,
  PER CHAR NOT NULL,
  PRC CHAR NOT NULL,
  DEV CHAR NOT NULL,
  PRIMARY KEY (id_stand)
);

CREATE TABLE STAND_USER
(
  id_user INT NOT NULL,
  user_name VARCHAR NOT NULL,
  id_stand INT NOT NULL,
  id_part INT NOT NULL,
  PRIMARY KEY (id_user),
  FOREIGN KEY (id_stand) REFERENCES STAND(id_stand),
  FOREIGN KEY (id_part) REFERENCES PART(id_part)
);

CREATE TABLE PART
(
  id_part INT NOT NULL,
  part_num INT NOT NULL,
  PRIMARY KEY (id_part),
);