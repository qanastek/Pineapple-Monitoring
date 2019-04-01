curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : "5EFF56A2AF15",
	"currentCpuLoad" : 1,
	"currentDiskUsage" : 1,
	"currentMemLoad" : 1,
	"currentSwapUsage" : 1,
	"currentConnectedUsers" : 1,
	"processCounter" : 1,
	"sysExp" : "linux",
	"coreCounter" : 6,
	"treadsCounter" : 12,
	"cpuModel" : "I9-7920X 2.9 Ghz",
	"hostName" : "Big Boy",
	"ram" : 2048,
	"disk" : 1024,
	"ram" : 2048
}' 'http://127.0.0.1:5000/api'