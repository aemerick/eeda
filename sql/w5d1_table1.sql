CREATE TABLE articles(
    id int,
    username varchar(12),
    time varchar(255),
    article_id int,
    PRIMARY KEY (id),
    UNIQUE (id)
  );

INSERT INTO articles
  (id, username, time, article_id)
VALUES
  (1,'john','2015-07-19 18:46:49',3),
  (2,'john','2015-07-19 18:46:52',2),
  (3,'john','2015-07-19 18:46:54',1),
  (4,'john','2015-07-19 18:46:58',10),
  (5,'john','2015-07-19 18:46:58',12),
  (6,'mike','2015-07-19 18:47:00',2),
  (7,'lori','2015-07-19 18:47:02',21),
  (8,'lori','2015-07-10 18:47:05',10),
  (9,'lori','2015-07-10 18:47:07',2);








