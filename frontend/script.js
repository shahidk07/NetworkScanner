function scan() {
    const ip = document.getElementById("ip").value;
    const range = document.getElementById("range").value;
    const mode = document.querySelector('input[name="mode"]:checked').value;
    const ipType = document.querySelector('input[name="iptype"]:checked').value;

    document.getElementById("status").innerText = "Scanning...";
    document.getElementById("results").innerHTML = "";

    fetch(`/scan?ip=${ip}&range=${range}&mode=${mode}`)
        .then(res => res.json())
        .then(data => {

            document.getElementById("status").innerText = "Scan complete";

            if (mode === "network") {
                // 🔥 network scan
                for (let host in data) {
                    for (let port in data[host]) {
                        let info = data[host][port];

                        let row = `
                            <tr>
                                <td>${host}</td>
                                <td>${port}</td>
                                <td>${info.protocol}</td>
                                <td>${info.service}</td>
                            </tr>
                        `;
                        document.getElementById("results").innerHTML += row;
                    }
                }
            } else {
                // 🔥 single scan
                for (let port in data) {
                    let info = data[port];

                    let row = `
                        <tr>
                            <td>-</td>
                            <td>${port}</td>
                            <td>${info.protocol}</td>
                            <td>${info.service}</td>
                        </tr>
                    `;
                    document.getElementById("results").innerHTML += row;
                }
            }
        })
        .catch(() => {
            document.getElementById("status").innerText = "Error scanning";
        });
}