# MentalHealthDB

Data Management System for Counseling at Schools

Built as part of Senior Year Project for AISSCE Internals.


MainMenu.py
- Main file: contains 6 menu options to view & alter records.
- Required functions are imported for use.

AddDel.py
- add(table) adds records to given 'table'.
- del(table) searches and deletes a given record from 'table'.

SearchModifyMove.py
- search(table, identity) searches for record with 'identity' in 'table'.
- modify(table, identity) finds record with 'identity' in 'table' and alters it.
- done(identity) effectively moves a student record from current matches to archives.
