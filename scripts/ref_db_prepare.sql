-- Create Element Sets
insert into ELEMENT_SET values((SELECT max(est_id)+1 FROM ELEMENT_SET),'AutoElementSet1','N','N',1,1);
insert into ELEMENT_SET values((SELECT max(est_id)+1 FROM ELEMENT_SET),'AutoElementSet2','N','N',1,1);
insert into ELEMENT_SET values((SELECT max(est_id)+1 FROM ELEMENT_SET),'AutoElementSet3','N','N',1,1);

COMMIT;

-- Create Elements
INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet1'), 1, 93,
'AutoTestElement11', 'AutoTestElement11 (93, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'931', NULL, 'Y', 'N', 0, 'N', 'N', 1);
INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet1'), 1, 93,
'AutoTestElement12', 'AutoTestElement12 (93, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'932', NULL, 'Y', 'N', 0, 'N', 'N', 1);

INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet2'), 1, 140,
'AutoTestElement21', 'AutoTestElement11 (140, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'1401', NULL, 'Y', 'N', 0, 'N', 'N', 1);
INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet2'), 1, 25,
'AutoTestElement22', 'AutoTestElement12 (25, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'251', NULL, 'Y', 'N', 0, 'N', 'N', 1);

INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet3'), 1, 42,
'AutoTestElement31', 'AutoTestElement11 (42, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'421', NULL, 'Y', 'N', 0, 'N', 'N', 1);
INSERT INTO ELEMENT VALUES((select max(elt_id)+1 from ELEMENT), (select est_id from element_set where est_name='AutoElementSet3'), 1, 102,
'AutoTestElement32', 'AutoTestElement12 (102, 07/01/2019)', TIMESTAMP '2019-07-01 00:00:00.000000', TIMESTAMP '9999-01-01 23:59:59.000000',
'1021', NULL, 'Y', 'N', 0, 'N', 'N', 1);

COMMIT;
