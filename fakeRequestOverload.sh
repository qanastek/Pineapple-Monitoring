curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : "A402B9E53F44",
	"currentCpuLoad" : 100,
	"currentDiskUsage" : 100,
	"currentMemLoad" : 100,
	"currentSwapUsage" : 100,
	"currentConnectedUsers" : 100,
	"processCounter" : 1400
}' 'http://127.0.0.1:5000/'