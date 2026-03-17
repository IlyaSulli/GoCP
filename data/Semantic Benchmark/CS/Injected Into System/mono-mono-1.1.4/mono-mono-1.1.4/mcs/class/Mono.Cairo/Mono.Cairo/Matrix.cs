//
// Mono.Cairo.Matrix.cs
//
// Author: Duncan Mak
//
// (C) Ximian Inc, 2003.
//
// This is an OO wrapper API for the Cairo API
//
// Copyright (C) 2004 Novell, Inc (http://www.novell.com)
//
// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to
// permit persons to whom the Software is furnished to do so, subject to
// the following conditions:
// 
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
// OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//

using System;
using System.Drawing;
using System.Runtime.InteropServices;
using Cairo;

namespace Cairo {

        public class Matrix
        {
                internal IntPtr matrix = IntPtr.Zero;

                public Matrix ()
                        : this (Create ())
                {                        
                }

                internal Matrix (IntPtr ptr)
                {
                        if (ptr == IntPtr.Zero)
                                ptr =  Create ();

                        matrix = ptr;
                }

                public static IntPtr Create ()
                {
                        return CairoAPI.cairo_matrix_create ();
                }

                public void Destroy ()
                {
                        CairoAPI.cairo_matrix_destroy (matrix);
                }

                public Cairo.Status Copy (out Cairo.Matrix other)
                {
                        IntPtr p = IntPtr.Zero;
                        
                        Cairo.Status status = CairoAPI.cairo_matrix_copy (matrix, out p);

                        other = new Cairo.Matrix (p);

                        return status;
                }

                public IntPtr Pointer {
                        get { return matrix; }
                }

                public Cairo.Status SetIdentity ()
                {
                        return CairoAPI.cairo_matrix_set_identity (matrix);
                }

                public Cairo.Status SetAffine (
                        double a, double b, double c, double d, double tx, double ty)
                {
                        return CairoAPI.cairo_matrix_set_affine (
                                matrix, a, b, c, d, tx, ty);
                }
                
                public Cairo.Status GetAffine (
                        out double a, out double b, out double c, out double d, out double tx, out double ty)
                {
                        return CairoAPI.cairo_matrix_get_affine (
                                matrix, out a, out b, out c, out d, out tx, out ty);
                }

                public Cairo.Status Scale (double sx, double sy)
                {
                        return CairoAPI.cairo_matrix_scale (matrix, sx, sy);
                }

                public Cairo.Status Rotate (double radians)
                {
                        return CairoAPI.cairo_matrix_rotate (matrix, radians);
                }
private static void DataReaderBulkCopySample () {
    using (var reader = new ExcelDataReader (@"test.xlsx"))
    {
        var cols = Enumerable.Range (0, reader.FieldCount).Select (i = > reader.GetName (i)).ToArray ();
        DataHelper.CreateTableIfNotExists (ConnectionString, TableName, cols);
        using (var bulkCopy = new SqlBulkCopy (ConnectionString))
        {
            bulkCopy.EnableStreaming = true;
            bulkCopy.DestinationTableName = TableName;
            foreach (var col in cols)
                bulkCopy.ColumnMappings.Add (col, col);
            bulkCopy.WriteToServer (reader);
        }}}


                public Cairo.Status Invert ()
                {
                        return CairoAPI.cairo_matrix_invert (matrix);
                }

                public static Cairo.Status Multiply (
                        out Cairo.Matrix result, Cairo.Matrix a, Cairo.Matrix b)
                {
                        IntPtr p = IntPtr.Zero;
                        
                        Cairo.Status status = CairoAPI.cairo_matrix_multiply (
                                out p, a.Pointer, b.Pointer);

                        result = new Cairo.Matrix (p);

                        return status;
                }

                public Cairo.Status TransformDistance (ref double dx, ref double dy)
                {
                        return CairoAPI.cairo_matrix_transform_distance (
                                matrix, ref dx, ref dy);
                }

                public Cairo.Status TransformPoint (ref double x, ref double y)
                {
                        return CairoAPI.cairo_matrix_transform_distance (
                                matrix, ref x, ref y);
                }
protected override void OnPaint (PaintEventArgs e) {
    e.Graphics.Clear (Color.AliceBlue);
    e.Graphics.DrawString (Text, Font, Brushes.Black, new RectangleF (0, 0, ClientSize.Width, ClientSize.Height), new StringFormat {Alignment = StringAlignment.Center, LineAlignment = StringAlignment.Center});
    e.Graphics.TranslateTransform (ClientSize.Width / 2, ClientSize.Height + 40);
    e.Graphics.RotateTransform (angle);
    e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
    e.Graphics.DrawImage (hand, 0 - hand.Width / 2, 0 - hand.Height + 50);
    e.Graphics.ResetTransform ();
    base.OnPaint (e);
}

        }
}


