package main

// Copyright (C) 2017  Jan Wollschläger <jmw.tau@gmail.com>
// This file is part of goccs.
//
// goccs is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

import (
        "testing"
      )

// Given a line in parametric form and a sphere, lineSphereIntersections
// should return the parameters of the line sphere intersection or
// false, if there is no intersection.
func TestLineSphereIntersections(t *testing.T) {
    logTestName("TestLineSphereIntersections")

    logTest("given a line (0,0,0) + t*(0,0,1)")
    lne := line{ origin: vec3{x: 0, y: 0, z: 0},
                 direction: vec3{x: 0, y: 0, z: 1},
                }
    logTest("and a sphere with radius 1 at (0,0,3)")
    sph := sphere{ center: vec3{x: 0, y: 0, z: 3},
                   radius: 1,
                 }
    i1, i2, _ := lineSphereIntersections(lne, sph)
    assertTrue(i1 == 2 && i2 == 4, "the intersections should be t = 2,4", t)


}































//