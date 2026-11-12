const samplePolicies = [
    {
        id: 1,
        name: "Health Insurance",
        premium: 5000
    },
    {
        id: 2,
        name: "Life Insurance",
        premium: 7500
    },
    {
        id: 3,
        name: "Vehicle Insurance",
        premium: 3000
    }
];

document.getElementById("loadPolicies")
.addEventListener("click", () => {

    const policyList =
        document.getElementById("policyList");

    policyList.innerHTML = "";

    samplePolicies.forEach(policy => {

        const div = document.createElement("div");
        div.className = "policy-card";

        div.innerHTML = `
            <h3>${policy.name}</h3>
            <p>Policy ID: ${policy.id}</p>
            <p>Premium: ₹${policy.premium}</p>
        `;

        policyList.appendChild(div);
    });
});