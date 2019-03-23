curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : 80010000,
	"currentCpuLoad" : 100,
	"currentDiskUsage" : 100,
	"currentMemLoad" : 100,
	"currentSwapUsage" : 100,
	"currentConnectedUsers" : 30,
	"processCounter" : 1400
}' 'http://127.0.0.1:5000/'