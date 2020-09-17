Module neptune.internal.hardware.gauges.gauge
=============================================

Classes
-------

`Gauge()`
:   

    ### Descendants

    * neptune.internal.hardware.gauges.cpu.CGroupCpuUsageGauge
    * neptune.internal.hardware.gauges.cpu.SystemCpuUsageGauge
    * neptune.internal.hardware.gauges.gpu.GpuMemoryGauge
    * neptune.internal.hardware.gauges.gpu.GpuUsageGauge
    * neptune.internal.hardware.gauges.memory.CGroupMemoryUsageGauge
    * neptune.internal.hardware.gauges.memory.SystemMemoryUsageGauge

    ### Methods

    `name(self)`
    :   :return: Gauge name (str).

    `value(self)`
    :   :return: Current value (float).