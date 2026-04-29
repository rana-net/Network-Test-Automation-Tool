def validate_output(output, test_type):

    output = output.lower()

    # 🔹 Ping Test
    if test_type == "ping":
        if "ttl" in output or "bytes from" in output:
            return "PASS"
        return "FAIL"

    # 🔹 Routing Table Test
    elif test_type == "routing":
        if "default" in output or "0.0.0.0" in output:
            return "PASS"
        return "FAIL"

    # 🔹 Open Ports Test
    elif test_type == "ports":
        if any(word in output for word in ["listen", "tcp", "udp"]):
            return "PASS"
        return "FAIL - No Open Ports"

    # 🔹 Traceroute Test
    elif test_type == "traceroute":
        if "traceroute" in output or "hop" in output or "1 " in output:
            return "PASS"
        return "FAIL"

    # 🔹 Unknown Test
    else:
        return "UNKNOWN TEST"