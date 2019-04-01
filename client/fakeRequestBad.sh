curl -XPOST -H "Content-type: application/json" -d '{
	"mac" : "5EFF56A2AF15",
	"currentCpuLoad" : "yanis",
	"disk" : 1,
	"currentMemLoad" : 1,
	"currentSwapUsage" : 1,
	"currentConnectedUsers" : 1,
	"test" : 1,
	"sysExp" : "linux",
	"coreCounter" : 6,
	"cpuModel" : I9-7920X 2.9 Ghz,
	"hostName" : "Big Boy",
	"ram" : 2048
}' 'http://127.0.0.1:5000/api'