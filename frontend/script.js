function scan() {
    const ip = document.getElementById("ip").value;
    const range = document.getElementById("range").value;

    const ipType = document.querySelector('input[name="iptype"]:checked').value;

    document.getElementById("status").innerText = "Scanning...";
    document.getElementById("results").innerHTML = "";

    fetch(`/scan?ip=${ip}&range=${range}`)
        .then(res => res.json())
        .then(data => {

            document.getElementById("status").innerText = "Scan complete";

            for (let port in data) {
                let row = `
                    <tr>
                        <td>${port}</td>
                        <td>${data[port].protocol}</td>
                        <td>${data[port].service}</td>
                    </tr>
                `;
                document.getElementById("results").innerHTML += row;
            }
        })
        .catch(() => {
            document.getElementById("status").innerText = "Error scanning";
        });
}