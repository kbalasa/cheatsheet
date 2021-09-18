create or replace function isnumeric (aval VARCHAR(20000))
  returns bool
IMMUTABLE 
as $$
    try:
       x = int(aval);
    except:
       return (1==2);
    else:
       return (1==1);
$$ language plpythonu;

