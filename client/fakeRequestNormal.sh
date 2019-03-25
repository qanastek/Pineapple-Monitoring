curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : "5EFF56A2AF15",
	"currentCpuLoad" : 1,
	"currentDiskUsage" : 1,
	"currentMemLoad" : 1,
	"currentSwapUsage" : 1,
	"currentConnectedUsers" : 1,
	"processCounter" : 1
}' 'http://127.0.0.1:5000/'