import { ArrowCircleRight2 } from "iconsax-react";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 min-h-screen justify-center items-center">
      <div className="m-3 text-8xl italic">모고<br />모고</div>
      <a href="/go" className="flex flex-row justify-between items-center gap-1 hover:underline font-semibold">
        <ArrowCircleRight2 color="#000" size={20} />
        변형 문제 풀러 가기
      </a>
    </div>
  );
}
