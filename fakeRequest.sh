curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : 80010000,
	"currentCpuLoad" : 10,
	"currentDiskUsage" : 10,
	"currentMemLoad" : 10,
	"currentSwapUsage" : 10,
	"currentConnectedUsers" : 3,
	"processCounter" : 14
}' 'http://127.0.0.1:5000/'