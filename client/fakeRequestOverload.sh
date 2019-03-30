curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : "A402B9E53F44",
	"currentCpuLoad" : 100,
	"currentDiskUsage" : 100,
	"currentMemLoad" : 100,
	"currentSwapUsage" : 100,
	"currentConnectedUsers" : 100,
	"processCounter" : 1400,
	"sysExp" : "linux",
	"coreCounter" : 6,
	"treadsCounter" : 12,
	"cpuModel" : "I9-7920X 2.9 Ghz",
	"hostName" : "Big Boy"
}' 'http://127.0.0.1:5000/api'