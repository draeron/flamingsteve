// Code generated by go-enum
// DO NOT EDIT!

package main

import (
	"fmt"
	"strings"
)

const (
	// SensorTypeNone is a SensorType of type None
	SensorTypeNone SensorType = iota + -1
	// SensorTypeAk9753 is a SensorType of type Ak9753
	SensorTypeAk9753
	// SensorTypeAmg8833 is a SensorType of type Amg8833
	SensorTypeAmg8833
)

const _SensorTypeName = "Noneak9753amg8833"

var _SensorTypeNames = []string{
	_SensorTypeName[0:4],
	_SensorTypeName[4:10],
	_SensorTypeName[10:17],
}

// SensorTypeNames returns a list of possible string values of SensorType.
func SensorTypeNames() []string {
	tmp := make([]string, len(_SensorTypeNames))
	copy(tmp, _SensorTypeNames)
	return tmp
}

var _SensorTypeMap = map[SensorType]string{
	-1: _SensorTypeName[0:4],
	0:  _SensorTypeName[4:10],
	1:  _SensorTypeName[10:17],
}

// String implements the Stringer interface.
func (x SensorType) String() string {
	if str, ok := _SensorTypeMap[x]; ok {
		return str
	}
	return fmt.Sprintf("SensorType(%d)", x)
}

var _SensorTypeValue = map[string]SensorType{
	_SensorTypeName[0:4]:   -1,
	_SensorTypeName[4:10]:  0,
	_SensorTypeName[10:17]: 1,
}

// ParseSensorType attempts to convert a string to a SensorType
func ParseSensorType(name string) (SensorType, error) {
	if x, ok := _SensorTypeValue[name]; ok {
		return x, nil
	}
	return SensorType(0), fmt.Errorf("%s is not a valid SensorType, try [%s]", name, strings.Join(_SensorTypeNames, ", "))
}

// Set implements the Golang flag.Value interface func.
func (x *SensorType) Set(val string) error {
	v, err := ParseSensorType(val)
	*x = v
	return err
}

// Get implements the Golang flag.Getter interface func.
func (x *SensorType) Get() interface{} {
	return *x
}

// Type implements the github.com/spf13/pFlag Value interface.
func (x *SensorType) Type() string {
	return "SensorType"
}
