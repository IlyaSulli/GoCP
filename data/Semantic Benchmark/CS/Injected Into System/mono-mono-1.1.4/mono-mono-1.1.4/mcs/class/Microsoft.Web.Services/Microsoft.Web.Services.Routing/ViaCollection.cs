//
// Microsoft.Web.Services.Routing.ViaCollection.cs
//
// Author: Daniel Kornhauser <dkor@alum.mit.edu>
//
// Copyright (C) Ximian, Inc. 2003
//

using System;
using System.Collections;

namespace Microsoft.Web.Services.Routing {
	
	public class ViaCollection : ICollection, IEnumerable, ICloneable
	{
		ArrayList list;

		public ViaCollection ()
		{
			list = new ArrayList ();
		}

	        ViaCollection (ArrayList list)
		{
			this.list = list;
		}

				
		public int Count { 
			get { return list.Count; }
		}


		public bool IsSynchronized {
			get { return list.IsSynchronized; }
		}


		public Via this [int filter] {
			get {
				return (Via) list [filter];
			}
			set {
				list[filter] = value;
			}

		}
		
		public virtual object SyncRoot {
			get {
				return list.SyncRoot;
			}
		}
		
		public int Add (Via via)
		{
			return list.Add (via);
		}
		
		public virtual object Clone ()
		{
			return new ViaCollection (list);
		}

		public virtual void CopyTo (Array array, int index) 
		{
			list.CopyTo(array, index);
		}

		public virtual IEnumerator GetEnumerator () 
		{
			return list.GetEnumerator();
		}

		public void Insert (int index, Via via) 
		{
			list.Insert(index, via);
		}
private static void AppendToDocument (string sourcePdfPath1, string sourcePdfPath2, string outputPdfPath) {
    using (var sourceDocumentStream1 = new FileStream (sourcePdfPath1, FileMode.Open))
    {
        using (var sourceDocumentStream2 = new FileStream (sourcePdfPath2, FileMode.Open))
        {
            using (var destinationDocumentStream = new FileStream (outputPdfPath, FileMode.Create))
            {
                var pdfConcat = new PdfConcatenate (destinationDocumentStream);
                var pdfReader = new PdfReader (sourceDocumentStream1);
                var pages = new List < int > ();
                for (int i = 0; i < pdfReader.NumberOfPages; i ++) {
                    pages.Add (i);
                }
                pdfReader.SelectPages (pages);
                pdfConcat.AddPages (pdfReader);
                pdfReader = new PdfReader (sourceDocumentStream2);
                pages = new List < int > ();
                for (int i = 0; i < pdfReader.NumberOfPages; i ++) {
                    pages.Add (i);
                }
                pdfReader.SelectPages (pages);
                pdfConcat.AddPages (pdfReader);
                pdfReader.Close ();
                pdfConcat.Close ();
            }}}}

int [] getRGB (Bitmap bmp, int line) {
    var data = bmp.LockBits (new Rectangle (0, 0, bmp.Width, bmp.Height), System.Drawing.Imaging.ImageLockMode.ReadOnly, System.Drawing.Imaging.PixelFormat.Format32bppRgb);
    try {
        var ptr = (IntPtr) ((long) data.Scan0 + data.Stride * (bmp.Height - line - 1));
        var ret = new int [bmp.Width];
        System.Runtime.InteropServices.Marshal.Copy (ptr, ret, 0, ret.Length * 4);
        return ret;
    }
    finally {
        bmp.UnlockBits (data);
    }
}


		public void InsertRange (int index, ViaCollection collection) 
		{
			list.InsertRange(index, collection);
		}

		public void RemoveAt (int index)
		{
			list.RemoveAt(index);
		}
	}
}


