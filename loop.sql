DO $$
BEGIN
    FOR i IN 1..20 LOOP
    	INSERT INTO STAND (id_stand, stand_name, PWR, SPD, RNG, PER, RPC, DEV) VALUES (i, 'stand' || i, 'A', 'A', 'A', 'A', 'A', 'A');
    END LOOP;
END $$;