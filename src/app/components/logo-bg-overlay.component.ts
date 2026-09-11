import { Component, OnInit, OnDestroy, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Particle {
  baseX: number;
  baseY: number;
  baseZ: number;
  rotSpeed: number;
  currentZ: number;
  style: any;
}

@Component({
  selector: 'app-logo-bg-overlay',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div id="logo-bg-overlay">
      <div *ngFor="let p of particles" 
        class="global-logo-particle"
        [ngStyle]="p.style">
      </div>
    </div>
  `
})
export class LogoBgOverlayComponent implements OnInit, OnDestroy {
  particles: Particle[] = [];
  private animFrameId: number | null = null;

  ngOnInit() {
    this.initParticles();
    this.updatePositions();
  }

  ngOnDestroy() {
    if (this.animFrameId !== null) {
      cancelAnimationFrame(this.animFrameId);
    }
  }

  @HostListener('window:scroll', [])
  onScroll() {
    this.updatePositions();
  }

  private initParticles() {
    const total = 20;
    this.particles = [];

    for (let i = 0; i < total; i++) {
      const baseX = 6 + (i % 5) * 20 + (Math.random() * 8 - 4);
      const baseY = 8 + Math.floor(i / 5) * 24 + (Math.random() * 10 - 5);
      const baseZ = -750 + (i * 70);
      const rotSpeed = 0.2 + Math.random() * 0.4;
      const size = 64 + (i % 4) * 16; // Varied sizes 64px, 80px, 96px, 112px

      this.particles.push({
        baseX,
        baseY,
        baseZ,
        rotSpeed,
        currentZ: baseZ,
        style: {
          width: `${size}px`,
          height: `${size}px`
        }
      });
    }
  }

  private updatePositions() {
    const scrollY = window.scrollY || window.pageYOffset || 0;
    const loopSpan = 1200;

    this.particles.forEach((p, i) => {
      let z = p.baseZ + scrollY * 0.85;
      let shiftCount = Math.floor((z - (-750)) / loopSpan);
      let currentZ = z - (shiftCount * loopSpan);
      if (currentZ > 450) currentZ -= loopSpan;
      if (currentZ < -750) currentZ += loopSpan;

      const normZ = (currentZ - (-750)) / 1200;
      let opacity = 0;
      if (normZ < 0.15) opacity = normZ / 0.15;
      else if (normZ > 0.82) opacity = (1 - normZ) / 0.18;
      else opacity = 1;

      // Noticeable, rich visibility (up to 24% opacity)
      opacity = Math.max(0, Math.min(0.24, opacity * 0.24));
      const rot = (scrollY * p.rotSpeed + i * 30) % 360;

      p.style = {
        ...p.style,
        left: p.baseX + '%',
        top: p.baseY + '%',
        transform: `translate3d(0, 0, ${currentZ}px) rotate(${rot}deg)`,
        opacity: opacity
      };
    });
  }
}
