<template>
  <div class="header-diagram-wrapper">
    <!-- Java 21 -->
    <div class="version-row">
      <div class="version-label">Java 21:</div>
      <div class="outer-container">
        <div class="inner-blocks">
          <!-- Class Word Section -->
          <div class="block pink" style="width: 160px;">
            <span class="internal-label">Compressed class pointer (32bits)</span>
            <span class="bottom-label">32 bit Class Word</span>
          </div>

          <!-- Separation Line -->
          <div class="section-divider"></div>

          <!-- Mark Word Section -->
          <div class="mark-word-group">
            <div class="block blue" style="width: 155px;">
              <span class="internal-label">Hash code (31 bits)</span>
            </div>
            <div class="block grey" style="width: 125px;">
              <span class="internal-label">Unused (25 bits)</span>
            </div>
            <div class="bars-container">
              <div class="bar-group">
                <span class="top-label orange">GC Age</span>
                <div class="bar-strip">
                  <div class="bar orange"></div>
                  <div class="bar orange"></div>
                  <div class="bar orange"></div>
                  <div class="bar orange"></div>
                </div>
              </div>
              <div class="bar-group">
                <span class="top-label green">Tag</span>
                <div class="bar-strip">
                  <div class="bar green"></div>
                  <div class="bar green"></div>
                  <div class="bar green"></div>
                </div>
              </div>
            </div>
            <span class="bottom-label mark-word-footer">64 bit Mark Word</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Java 24+ -->
    <div class="version-row mt-12">
      <div class="version-label">Java <br/> 24+:</div>
      <div class="outer-container">
        <div class="inner-blocks">
          <div class="block pink" style="width: 110px;">
            <span class="internal-label small-text">Compressed class pointer (22bits)</span>
          </div>
          <div class="block blue" style="width: 155px;">
            <span class="internal-label">Hash code (31 bits)</span>
          </div>
          <div class="block grey" style="width: 45px;">
            <span class="internal-label x-small-text">Unused (4 bits)</span>
          </div>
          <div class="bars-container">
            <div class="bar-group">
              <span class="top-label orange">GC Age</span>
              <div class="bar-strip">
                <div class="bar orange"></div>
                <div class="bar orange"></div>
                <div class="bar orange"></div>
                <div class="bar orange"></div>
              </div>
            </div>
            <div class="bar-group">
              <span class="top-label green">Tag</span>
              <div class="bar-strip">
                <div class="bar green"></div>
                <div class="bar green"></div>
                <div class="bar green"></div>
              </div>
            </div>
          </div>
        </div>
        <span class="footer-label">64 bit object pointer</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header-diagram-wrapper {
  --px: min(calc(100cqw / 1280), calc(100cqh / 720));
  width: 100%;
  max-width: fit-content;
  margin: 0 auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  padding-top: 30px;
}

.version-row {
  display: flex;
  align-items: center;
  gap: 25px;
  width: fit-content;
}

.version-label {
  font-size: 1.8rem;
  font-weight: 800;
  color: #a1a1aa;
  line-height: 0.95;
  text-align: right;
  min-width: 120px;
}

.outer-container {
  position: relative;
  background: #111111;
  border: 1.5px solid #3f3f46;
  border-radius: 10px;
  padding: 6px;
  width: fit-content;
}

.inner-blocks {
  display: flex;
  align-items: center;
  height: 60px;
  width: fit-content;
}

.mark-word-group {
  display: flex;
  align-items: center;
  height: 100%;
  position: relative;
  width: fit-content;
}

.section-divider {
  width: 0;
  height: 85%;
  border-left: 2px dotted #71717a;
  margin: 0 10px;
}

.block {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  border: 1.5px dashed transparent;
  margin: 0 1px;
  padding: 0 5px;
}

.block.pink {
  border-color: #f472b6;
  background: rgba(244, 114, 182, 0.12);
}
.block.pink .internal-label { color: #f472b6; }

.block.blue {
  border-color: #60a5fa;
  background: rgba(96, 165, 250, 0.12);
}
.block.blue .internal-label { color: #60a5fa; }

.block.grey {
  border-color: #52525b;
  background: rgba(255, 255, 255, 0.05);
}
.block.grey .internal-label { color: #94a3b8; }

.internal-label {
  font-size: 9px;
  font-weight: 700;
  text-align: center;
  line-height: 1.1;
  word-break: break-word;
}

.internal-label.small-text {
  font-size: 8px;
}

.internal-label.x-small-text {
  font-size: 7px;
}

.top-label {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  font-size: 10px;
  font-weight: 700;
  white-space: nowrap;
  top: -22px;
}

.bottom-label {
  position: absolute;
  bottom: -29px;
  font-size: 11px;
  font-weight: 500;
  color: #94a3b8;
  white-space: nowrap;
}

.mark-word-footer {
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  text-align: center;
}

.bars-container {
  display: flex;
  gap: 10px;
  padding: 0 10px;
  align-items: center;
}

.bar-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.bar-strip {
  display: flex;
  gap: 3px;
}

.bar {
  width: 8px;
  height: 24px;
  border-radius: 2px;
}

.bar.orange { background-color: #fb923c; }
.bar.green { background-color: #4ade80; }

.top-label.orange { color: #fb923c; }
.top-label.green { color: #4ade80; }

.footer-label {
  position: absolute;
  bottom: -22px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 12px;
  font-weight: 500;
  color: #94a3b8;
  white-space: nowrap;
}

.mt-12 { margin-top: 60px; }
</style>
