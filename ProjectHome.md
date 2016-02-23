OraPIG generates Python wrapper classes for Oracle PL/SQL packages.

Full docs: http://www.markharrison.net/orapig

This package:
```
  create or replace package tiny
  --+ this is a tiny package
  as
      --+ p is the only procedure
      procedure p(x in number);
  end tiny;
```
creates this class:
```
  class Tiny:
      """this is a tiny package"""  # from --+ docstring
      def __init__(self,curs):      # instantiate class with a cursor
          ...
      def p(self,x):                # call procedure tiny.p(x)
          """p is the only procedure"""
          ...
```
which can be used like this:
```
  curs = conn.cursor()
  mytiny = tiny.Tiny(curs)
  mytiny.p(2)           # call a procedure
  curs.commit()         # not done automatically
```