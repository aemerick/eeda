import sys



if len(sys.argv) > 1:
     workdir = str( sys.argv[1] )

     a = int( sys.argv[2] )
     b = int( sys.argv[3] )

print(workdir)
print(a+b)
