SET SERVEROUTPUT ON;
DECLARE
   l_today_date        DATE := SYSDATE;
   l_today_timestamp   TIMESTAMP := SYSTIMESTAMP;
BEGIN
    DBMS_OUTPUT.put_line (SYSTIMESTAMP);
    DBMS_OUTPUT.put_line (l_today_date);
END;