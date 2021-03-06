-- This file is part of the ESP Web Site
-- Copyright (c) Adam Seering 2009
--
-- The ESP Web Site is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
-- 
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
-- 
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
-- 
-- Contact Us:
-- ESP Web Group
-- MIT Educational Studies Program,
-- 84 Massachusetts Ave W20-467, Cambridge, MA 02139
-- Phone: 617-253-4882
-- Email: web@esp.mit.edu


-- ***
-- Table indices for the UserBit table
-- ***

-- Force UserBits to be unique
CREATE INDEX userbit__user_lookup ON users_userbit USING btree (user_id);
CREATE INDEX userbit_startdate ON users_userbit USING btree (startdate);
CREATE INDEX userbit_enddate ON users_userbit USING btree (enddate);
