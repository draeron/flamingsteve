// Code generated by go-enum
// DO NOT EDIT!

package amg8833

import (
	"fmt"
	"strings"
)

const (
	// ErrorNone is a Error of type None
	ErrorNone Error = iota
	// ErrorParam is a Error of type Param
	ErrorParam Error = iota + -2
	// ErrorComm is a Error of type Comm
	ErrorComm Error = iota + -4
	// ErrorOther is a Error of type Other
	ErrorOther Error = iota + -131
)

const _ErrorName = "NoneParamCommOther"

var _ErrorNames = []string{
	_ErrorName[0:4],
	_ErrorName[4:9],
	_ErrorName[9:13],
	_ErrorName[13:18],
}

// ErrorNames returns a list of possible string values of Error.
func ErrorNames() []string {
	tmp := make([]string, len(_ErrorNames))
	copy(tmp, _ErrorNames)
	return tmp
}

var _ErrorMap = map[Error]string{
	0:    _ErrorName[0:4],
	-1:   _ErrorName[4:9],
	-2:   _ErrorName[9:13],
	-128: _ErrorName[13:18],
}

// String implements the Stringer interface.
func (x Error) String() string {
	if str, ok := _ErrorMap[x]; ok {
		return str
	}
	return fmt.Sprintf("Error(%d)", x)
}

var _ErrorValue = map[string]Error{
	_ErrorName[0:4]:   0,
	_ErrorName[4:9]:   -1,
	_ErrorName[9:13]:  -2,
	_ErrorName[13:18]: -128,
}

// ParseError attempts to convert a string to a Error
func ParseError(name string) (Error, error) {
	if x, ok := _ErrorValue[name]; ok {
		return x, nil
	}
	return Error(0), fmt.Errorf("%s is not a valid Error, try [%s]", name, strings.Join(_ErrorNames, ", "))
}
