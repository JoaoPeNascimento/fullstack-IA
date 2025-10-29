export default function SummaryOutput({ result }) {
  if (!result) return null;

  return (
    <div className="w-full max-w-2xl bg-white/10 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/20 mt-6">
      <h2 className="text-xl font-bold text-indigo-300 mb-3">
        Resultado da Análise
      </h2>
      <p className="text-gray-100 leading-relaxed whitespace-pre-line">
        {result}
      </p>
    </div>
  );
}
