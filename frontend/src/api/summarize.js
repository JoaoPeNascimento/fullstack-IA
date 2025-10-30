import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export const summarizeText = async (inputText) => {
  try {
    console.log(API_URL);
    const response = await axios.post(`${API_URL}/analyze`, {
      task: "summarize",
      input_text: inputText,
      use_external: false,
      options: { lang: "pt" },
    });
    return response.data;
  } catch (error) {
    console.error(
      "Erro ao resumir texto:",
      error.response?.data || error.message
    );
    throw error;
  }
};
