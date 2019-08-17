-- Perform Cleanup of Elements and Element Sets
delete from band;
delete from element_connection;
delete from element where elt_name like 'AutoTestElement%';
delete from element_set where est_name like 'AutoElementSet%';
commit;
