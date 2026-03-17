//
// ReplayCacheManager.cs - ReplayCache Manager
//
// Author:
//	Sebastien Pouliot (spouliot@motus.com)
//
// (C) 2003 Motus Technologies Inc. (http://www.motus.com)
//

using System;

namespace Microsoft.Web.Services.Security {

	public class ReplayCacheManager {

		public ReplayCacheManager () {}

		[MonoTODO]
		public static void ProcessMessage (SoapEnvelope envelope) {}
public static GraphicsPath Shrink (this GraphicsPath path, float width) {
    using (var p = new GraphicsPath ())
    {
        p.AddPath (path, false);
        p.CloseAllFigures ();
        p.Widen (new Pen (Color.Black, width * 2));
        var position = 0;
        var result = new GraphicsPath ();
        while (position < p.PointCount) {
            position += CountNextFigure (p.PathData, position);
            var figureCount = CountNextFigure (p.PathData, position);
            var points = new PointF [figureCount];
            var types = new byte [figureCount];
            Array.Copy (p.PathPoints, position, points, 0, figureCount);
            Array.Copy (p.PathTypes, position, types, 0, figureCount);
            position += figureCount;
            result.AddPath (new GraphicsPath (points, types), false);
        }
        path.Reset ();
        path.AddPath (result, false);
        return path;
    }}

	}
}

