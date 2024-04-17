A Raspberry Pi is like a mini-computer that's both affordable and
powerful, perfect for learning how to code and for creative projects,
such as making a robot car move. To use a Raspberry Pi, it and your main
computer need to be able to "talk" to each other, which means they have
to be on the same digital network.

## How to Connect Your Raspberry Pi and Computer

### Option 1: Joining the Same Wi-Fi Network

-   **The Basics**: The simplest way to link your computer with the
    Raspberry Pi is by connecting both to the same Wi-Fi network. This
    can be the Wi-Fi at your home, school, or anywhere else you have
    access.

-   **Troubleshooting Tips**: If you're at school or work, you might not
    see your Raspberry Pi on the network due to extra security measures.
    If this happens (known as not being able to "ping" the Raspberry
    Pi), don't worry; just try the next solution.

### Option 2: Using a Mobile Hotspot (Recommended)

-   **Creating Your Network**: If the first method doesn't work, you can
    use your smartphone or computer to create a Wi-Fi network through a
    feature known as a hotspot.

    -   **For Windows Users**: Look up "How to set up a mobile hotspot
        in Windows 10/11" for detailed instructions.

    -   **For Linux Users**:

        -   Go to the system menu at the top right.

        -   Click the Wi-Fi symbol, then "All Networks".

        -   Click the menu in the top-right and choose "Turn On Wi-Fi
            Hotspot…".

        -   If asked to disconnect from your current Wi-Fi, click "Turn
            On" to proceed.

-   **Pro Tip**: If your Raspberry Pi struggles to connect, change the
    hotspot to use the 2.4GHz band for better device compatibility.

### Option 3: Direct Connection Using an Ethernet Cable

-   **For Setup Only**: You can connect your computer to the Raspberry
    Pi with an Ethernet cable, perfect for initial setups. However,
    Wi-Fi is needed for projects like controlling a robot car.

-   **Steps**:

    -   Connect one end of the Ethernet cable to your computer and the
        other to the Raspberry Pi.

    -   Use a command line or terminal to type `ping donkeypi.local`
        (substitute "donkeypi.local" with your Raspberry Pi's actual
        name).

    -   If possible, enable Internet Connection Sharing (ICS) on Windows
        or Ubuntu. This will allow you to share your WiFi connection
        from your Host PC to your Raspberry Pi over ethernet.

## Controlling Your Raspberry Pi Remotely

Once connected to the same network, you can control your Raspberry Pi
from your computer, using either the command line (SSH) or a graphical
interface (VNC).

### SSH (Secure Shell)

-   **What It Is**: SSH lets you send commands to your Raspberry Pi from
    your computer's terminal.

-   **How to Use It**:

    -   Make sure both devices are on the same network.

    -   Open a terminal and type `ssh <username>@<hostname>.local`
        (replace with your details, like `ssh donkey@donkeypi.local`).

### VNC (Virtual Network Computing)

-   **What It Is**: VNC allows you to view and interact with your
    Raspberry Pi's desktop from your computer, making graphical tasks
    easier.

-   **Setting It Up**:

    -   Download and install RealVNC viewer from their official website,
        selecting the version for your operating system.

    -   When installing, you can skip the sign-in step.

    -   Open VNC Viewer, create a new connection and type your Raspberry
        Pi's IP address or hostname. Use the password you set on your
        Raspberry Pi if prompted.

**Remember**: The hostname is a unique name you give your Raspberry Pi
during setup. It makes finding and connecting to your Raspberry Pi
easier on a network.

By following these simplified steps, you're now ready to embark on
exciting projects with your Raspberry Pi, from programming to building
and controlling your own robot car!

## Changing WiFi Settings

There are two main ways to adjust the network settings: through a
graphical interface (like the desktop you're accustomed to) or the
command line. We'll focus on the command line for its simplicity and
ease of use remotely via SSH (Secure Shell), which lets you control your
Pi from another computer.

### Basic Networking Commands

Here's a straightforward guide to some basic networking commands.
Remember, the command line takes what you type literally, so precision
is key.

-   **Check NetworkManager Status**

    -   The command `systemctl status NetworkManager` is essentially
        asking, "Is the NetworkManager service active?" NetworkManager
        is crucial as it handles all your network connections.

        ```bash title="Check NetworkManager Status"
        systemctl status NetworkManager
        ```

-   **Start NetworkManager**

    -   Using `sudo systemctl start NetworkManager` starts NetworkManager
        if it's not already running. The sudo signifies you're
        requesting to perform an action that requires administrator
        rights.

        ```bash title="Start NetworkManager"
        sudo systemctl start NetworkManager
        ```

-   **Restart NetworkManager**

    -   Sometimes, network connections can be finicky. Issuing `sudo systemctl restart NetworkManager` can help by resetting your
        network connections, akin to toggling WiFi on your smartphone.

        ```bash title="Restart NetworkManager"
        sudo systemctl restart NetworkManager
        ```

-   **List Available WiFi Networks**

    -   The command `nmcli dev wifi` prompts your device to list all WiFi
        networks within range, useful for spotting available
        connections.

        ```bash title="List Available WiFi Networks"
        nmcli dev wifi
        ```

-   **Connect to a WiFi Network**

    -   With `sudo nmcli dev wifi connect "SSID" password "PASSWORD"`, you
        can connect to a specific WiFi by replacing "SSID" with the
        network's name and "PASSWORD" with the network's password. Keep
        the quotation marks if your WiFi's name or password includes
        spaces or special characters.

        ```bash title="Connect to a WiFi Network"
        sudo nmcli dev wifi connect "SSID" password "PASSWORD"
        ```

-   **Check Your Connection Status**

    -   `sudo systemctl restart NetworkManager` lets you verify your network connection's
        status, ensuring everything is functioning as intended.

        ```bash title="Check Your Connection Status"
        sudo systemctl restart NetworkManager
        ```
