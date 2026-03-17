/*
 *  Firebird ADO.NET Data provider for .NET and Mono 
 * 
 *     The contents of this file are subject to the Initial 
 *     Developer's Public License Version 1.0 (the "License"); 
 *     you may not use this file except in compliance with the 
 *     License. You may obtain a copy of the License at 
 *     http://www.firebirdsql.org/index.php?op=doc&id=idpl
 *
 *     Software distributed under the License is distributed on 
 *     an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either 
 *     express or implied.  See the License for the specific 
 *     language governing rights and limitations under the License.
 * 
 *  Copyright (c) 2002, 2004 Carlos Guzman Alvarez
 *  All Rights Reserved.
 */

using System;
using System.Data;
using System.Collections;
using FirebirdSql.Data.Firebird;
using FirebirdSql.Data.Firebird.Isql;
using NUnit.Framework;

namespace FirebirdSql.Data.Firebird.Tests
{
    [TestFixture]
    public class FbDatabaseSchemaTest : BaseTest
    {
        public FbDatabaseSchemaTest() : base(false)
        {
        }

        [Test]
        public void CharacterSets()
        {
            Connection.GetSchema("CharacterSets");
        }

        [Test]
        public void CheckConstraints()
        {
            Connection.GetSchema("CheckConstraints");
        }

        [Test]
        public void CheckConstraintsByTable()
        {
            Connection.GetSchema("CheckConstraintsByTable");
        }

        [Test]
        public void Collations()
        {
            Connection.GetSchema("Collations");
        }

        [Test]
        public void Columns()
        {
            DataTable columns = Connection.GetSchema("Columns");

            columns = Connection.GetSchema(
                            "Columns",
                            new string[] { null, null, "TEST", "INT_FIELD" });

            Assert.AreEqual(1, columns.Rows.Count);
        }
private void dateTimePicker1_ValueChanged (object sender, EventArgs e) {
    int gyear = dateTimePicker1.Value.Year;
    int gmonth = dateTimePicker1.Value.Month;
    int gday = dateTimePicker1.Value.Day;
    int syear = DateTime.Now.Year;
    int smonth = DateTime.Now.Month;
    int sday = DateTime.Now.Day;
    int difday = DateTime.DaysInMonth (syear, gmonth);
    agedisplay = (syear - gyear);
    lmonth = (smonth - gmonth);
    lday = (sday - gday);
    if (smonth < gmonth) {
        agedisplay = agedisplay - 1;
    }
    if (smonth == gmonth) {
        if (sday < (gday)) {
            agedisplay = agedisplay - 1;
        }
    }
    if (smonth < gmonth) {
        lmonth = (- (- smonth) + (- gmonth) + 12);
    }
    if (lday < 0) {
        lday = difday - (- lday);
        lmonth = lmonth - 1;
    }
    if (smonth == gmonth && sday < gday && gyear != syear) {
        lmonth = 11;
    }
    ageDisplay.Text = Convert.ToString (agedisplay) + " Years,  " + lmonth + " Months,  " + lday + " Days.";
}


        [Test]
        public void ColumnPrivileges()
        {
            Connection.GetSchema("ColumnPrivileges");
        }

        [Test]
        public void Domains()
        {
            Connection.GetSchema("Domains");
        }

        [Test]
        public void ForeignKeys()
        {
            Connection.GetSchema("ForeignKeys");
        }

        [Test]
        public void Functions()
        {
            Connection.GetSchema("Functions");
        }

        [Test]
        public void Generators()
        {
            Connection.GetSchema("Generators");
        }

        [Test]
        public void Indexes()
        {
            Connection.GetSchema("Indexes");
        }

        [Test]
        public void PrimaryKeys()
        {
            DataTable primaryKeys = Connection.GetSchema("PrimaryKeys");

            primaryKeys = Connection.GetSchema(
                "PrimaryKeys",
                new string[] { null, null, "TEST" });

            Assert.AreEqual(1, primaryKeys.Rows.Count);
        }

        [Test]
        public void ProcedureParameters()
        {
            Connection.GetSchema("ProcedureParameters");

            DataTable procedureParameters = Connection.GetSchema(
                "ProcedureParameters",
                new string[] { null, null, "SELECT_DATA" });

            Assert.AreEqual(3, procedureParameters.Rows.Count);
        }

        [Test]
        public void ProcedurePrivileges()
        {
            Connection.GetSchema("ProcedurePrivileges");
        }

        [Test]
        public void Procedures()
        {
            DataTable procedures = Connection.GetSchema("Procedures");

            procedures = Connection.GetSchema(
                "Procedures",
                new string[] { null, null, "SELECT_DATA" });

            Assert.AreEqual(1, procedures.Rows.Count);
        }

        [Test]
        public void DataTypes()
        {
            Connection.GetSchema("DataTypes");
        }

        [Test]
        public void Roles()
        {
            Connection.GetSchema("Roles");
        }

        [Test]
        public void Tables()
        {
            DataTable tables = Connection.GetSchema("Tables");

            tables = Connection.GetSchema(
                "Tables",
                new string[] { null, null, "TEST" });

            Assert.AreEqual(tables.Rows.Count, 1);

            tables = Connection.GetSchema(
                "Tables",
                new string[] { null, null, null, "TABLE" });

            Assert.AreEqual(tables.Rows.Count, 1);
        }

        [Test]
        public void TableConstraints()
        {
            Connection.GetSchema("TableConstraints");
        }

        [Test]
        public void TablePrivileges()
        {
            Connection.GetSchema("TablePrivileges");
        }

        [Test]
        public void Triggers()
        {
            Connection.GetSchema("Triggers");
        }

        [Test]
        public void UniqueKeys()
        {
            Connection.GetSchema("UniqueKeys");
        }

        [Test]
        public void ViewColumnUsage()
        {
            Connection.GetSchema("ViewColumnUsage");
        }

        [Test]
        public void Views()
        {
            Connection.GetSchema("Views");
        }

        [Test]
        public void ViewPrivileges()
        {
            Connection.GetSchema("ViewPrivileges");
        }
    }
}

