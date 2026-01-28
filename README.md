# mcu-ethernet-relay-ch9121

A TCP-controlled MCU system using a **CH9121 serial-to-Ethernet module** and a **Python TCP server**. The project enables remote digital I/O control and bidirectional UART communication over Ethernet, with live **temperature and humidity telemetry** from a **DHT11 sensor**.

▶️ **Project Demo (YouTube)**
[![Project Demo](https://img.youtube.com/vi/UsRj-GCuNJ0/0.jpg)](https://www.youtube.com/watch?v=UsRj-GCuNJ0)

---

## Overview

The MCU communicates with the CH9121 module via UART, allowing TCP/IP messages from a host PC to be translated into embedded commands. Incoming TCP commands can toggle GPIOs (e.g. driving a relay), while sensor data is streamed back to the server in real time.

This project serves as a reference design for **serial-to-Ethernet bridging**, **remote MCU control**, and **embedded sensor telemetry over TCP/IP**.

---

## Demo Setup

* The PC running the Python TCP server and the MCU (client) are connected to the **same LAN** via a router.
* The MCU is connected to the CH9121 module using UART.
* TCP messages sent from the PC toggle an MCU GPIO connected to a **relay**, which switches a high-power LED.
* Temperature and humidity data from a **DHT11 sensor** connected to the MCU is transmitted back to the PC.

---

## Key Features

* TCP-based remote MCU control
* CH9121 UART-to-Ethernet integration
* Python TCP server with interactive send/receive
* Bidirectional UART communication
* Remote relay / GPIO switching
* DHT11 temperature and humidity telemetry

---

## Resources

* Waveshare 2-CH UART TO ETH Wiki
  [https://www.waveshare.com/wiki/2-CH_UART_TO_ETH](https://www.waveshare.com/wiki/2-CH_UART_TO_ETH)
* CH9121 Datasheet (SPCC)
  [https://files.waveshare.com/upload/e/ef/CH9121_SPCC.pdf](https://files.waveshare.com/upload/e/ef/CH9121_SPCC.pdf)
* Using the CH9121 Module (BotBlox)
  [https://botblox.notion.site/Using-the-CH9121-Module-e63ebd64da8e4fbab551a79db56d6039](https://botblox.notion.site/Using-the-CH9121-Module-e63ebd64da8e4fbab551a79db56d6039)
* CH9121 Module Reference (ChinaLC Tech)
  [http://www.chinalctech.com/m/view.php?aid=468](http://www.chinalctech.com/m/view.php?aid=468)
