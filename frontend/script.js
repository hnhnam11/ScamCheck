const button = document.getElementById("analyzeButton");

const resultText = document.getElementById("resultText");

const messageInput = document.getElementById("messageInput");

button.addEventListener("click", async () => {
  const message = messageInput.value;

  if (!message) {
    alert("Vui lòng nhập nội dung");

    return;
  }

  resultText.innerHTML = "🔄 Đang phân tích...";

  try {
    const response = await fetch("https://YOUR-BACKEND.onrender.com/analyze", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message: message,
      }),
    });

    const result = await response.text();

    resultText.innerHTML = result;
  } catch (error) {
    resultText.innerHTML = "❌ Không thể kết nối máy chủ";

    console.error(error);
  }
});
