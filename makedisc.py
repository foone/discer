import math, random

SECTORS = 48
TRACKS = 24
SIZE = (800, 800)
MINRADIUS = 64
TRACKWIDTH = 12

def polarToCartesian(cx, cy, r, a):
  ar = (a-90)*math.pi / 180.0;
  return (cx + r * math.cos(ar), cy + r * math.sin(ar))

def describeArc(x, y, innerRadius, outerRadius, startAngle, endAngle):

  start = polarToCartesian(x, y, outerRadius, endAngle)
  start2 = polarToCartesian(x, y, innerRadius, endAngle)
  end = polarToCartesian(x, y, innerRadius, startAngle)
  end2 = polarToCartesian(x, y, outerRadius, startAngle)

  arcSweep = "0" if endAngle - startAngle <= 180 else "1"
  arcSweep2 = "0" if startAngle - endAngle <= 180 else "1"

  d=[

        "M", start[0], start[1], 
        "L", start2[0], start2[1],
        "A", innerRadius, innerRadius, 0, arcSweep, 0, end[0], end[1],
        "L", end2[0], end2[1],
        "A", outerRadius, outerRadius, 0, arcSweep, 1, start[0], start[1],
  ]
  return ' '.join(str(x) for x in d)


print '<svg xmlns="http://www.w3.org/2000/svg"  width="{}" height="{}">'.format(SIZE[0],SIZE[1])
sectorWidth = 360.0/SECTORS
for track in range(1+TRACKS):
  for sector in range(SECTORS):
    lowerTrack = MINRADIUS+TRACKWIDTH*track
    path = describeArc(SIZE[0]/2, SIZE[1]/2, lowerTrack,lowerTrack+TRACKWIDTH, sector*sectorWidth, (sector+1)*sectorWidth)
    color = random.choice(['black','white'])
    if track == 0:
      color = 'grey'
    print '<path fill="{}" stroke="{}" stroke-width="1" d="{}" />'.format(color, color, path)

print '</svg>'