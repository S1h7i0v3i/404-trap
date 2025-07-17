let ipChart;

async function fetchDates() {
  const res = await fetch('/api/dates');
  const dates = await res.json();
  const select = document.getElementById('dateSelect');
  select.innerHTML = '';
  dates.forEach(date => {
    const option = document.createElement('option');
    option.value = date;
    option.textContent = date;
    select.appendChild(option);
  });
}

async function fetchLogs() {
  const date = document.getElementById('dateSelect').value;
  const logRes = await fetch(`/api/logs?date=${date}`);
  const logs = await logRes.json();

  const statsRes = await fetch(`/api/stats?date=${date}`);
  const stats = await statsRes.json();

  updateStats(stats);
  updateChart(stats.top_ips);
  populateTable(logs);
}

function updateStats(stats) {
  document.getElementById('totalHits').textContent = stats.total_hits;
  document.getElementById('uniqueIPs').textContent = stats.unique_ips;
  document.getElementById('topPath').textContent = stats.top_path || '-';
}

function updateChart(topIps) {
  const ctx = document.getElementById('ipChart').getContext('2d');
  const labels = topIps.map(item => item[0]);
  const data = topIps.map(item => item[1]);

  if (ipChart) ipChart.destroy();
  ipChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Top Attacker IPs',
        data,
        backgroundColor: '#007bff'
      }]
    },
    options: { responsive: true }
  });
}

function populateTable(logs) {
  const tbody = document.getElementById('logTable');
  tbody.innerHTML = '';
  logs.forEach(line => {
    const match = line.match(/(\d+-\d+-\d+ \d+:\d+:\d+) - IP: ([^\s]+) - Location: ([^-]+) - Path: ([^\s]+) - UA: (.+)/);
    if (!match) return;
    const [, time, ip, location, path, ua] = match;
    const row = `<tr>
      <td>${time}</td>
      <td>${ip}</td>
      <td>${location}</td>
      <td>${path}</td>
      <td>${ua}</td>
    </tr>`;
    tbody.insertAdjacentHTML('beforeend', row);
  });
}


function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  document.body.classList.toggle('light-mode');
}

async function downloadCSV() {
  const date = document.getElementById('dateSelect').value;
  window.location.href = `/api/export-logs?date=${date}`;
}

// Initialize
(async () => {
  await fetchDates();
  await fetchLogs();
})();
