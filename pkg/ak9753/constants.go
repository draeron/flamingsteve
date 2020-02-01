package ak9753

type Cmd byte

func (c Cmd) toBytes() []byte {
	return []byte{byte(c)}
}

const (
  I2C_DEFAULT_ADDRESS = 0x64

  DEVICE_ID      = 0x13

  REG_WIA1       = 0x00
  REG_WIA2       = 0x01
  REG_INFO1      = 0x02
  REG_INFO2      = 0x03
  REG_INTST      = 0x04
  REG_ST1        = 0x05
  REG_IR1L       = 0x06
  REG_IR1H       = 0x07
  REG_IR2L       = 0x08
  REG_IR2H       = 0x09
  REG_IR3L       = 0x0A
  REG_IR3H       = 0x0B
  REG_IR4L       = 0x0C
  REG_IR4H       = 0x0D
  REG_TMPL       = 0x0E
  REG_TMPH       = 0x0F
  REG_ST2        = 0x10
  REG_ETH13H_LSB = 0x11
  REG_ETH13H_MSB = 0x12
  REG_ETH13L_LSB = 0x13
  REG_ETH13L_MSB = 0x14
  REG_ETH24H_LSB = 0x15
  REG_ETH24H_MSB = 0x16
  REG_ETH24L_LSB = 0x17
  REG_ETH24L_MSB = 0x18
  REG_EHYS13     = 0x19
  REG_EHYS24     = 0x1A
  REG_EINTEN     = 0x1B
  REG_ECNTL1     = 0x1C
  REG_CNTL2      = 0x1D

  /* EEPROM */
  REG_EKEY          = 0x50
  EEPROM_ETH13H_LSB = 0x51
  EEPROM_ETH13H_MSB = 0x52
  EEPROM_ETH13L_LSB = 0x53
  EEPROM_ETH13L_MSB = 0x54
  EEPROM_ETH24H_LSB = 0x55
  EEPROM_ETH24H_MSB = 0x56
  EEPROM_ETH24L_LSB = 0x57
  EEPROM_ETH24L_MSB = 0x58
  EEPROM_EHYS13     = 0x59
  EEPROM_EHYS24     = 0x5A
  EEPROM_EINTEN     = 0x5B
  EEPROM_ECNTL1     = 0x5C

  //Valid sensor modes - Register ECNTL1
  AK975X_MODE_STANDBY = 0b000
  AK975X_MODE_EEPROM_ACCESS = 0b001
  AK975X_MODE_SINGLE_SHOT = 0b010
  AK975X_MODE_0 = 0b100
  AK975X_MODE_1 = 0b101
  AK975X_MODE_2 = 0b110
  AK975X_MODE_3 = 0b111

  //Valid digital filter cutoff frequencies
  AK975X_FREQ_0_3HZ = 0b000
  AK975X_FREQ_0_6HZ = 0b001
  AK975X_FREQ_1_1HZ = 0b010
  AK975X_FREQ_2_2HZ = 0b011
  AK975X_FREQ_4_4HZ = 0b100
  AK975X_FREQ_8_8HZ = 0b101
)
