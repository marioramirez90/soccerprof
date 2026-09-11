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
    const total = 18;
    this.particles = [];

    for (let i = 0; i < total; i++) {
      const baseX = 8 + (i % 6) * 16 + (Math.random() * 8 - 4);
      const baseY = 10 + Math.floor(i / 6) * 28 + (Math.random() * 12 - 6);
      const baseZ = -700 + (i * 65);
      const rotSpeed = 0.15 + Math.random() * 0.35;

      this.particles.push({
        baseX,
        baseY,
        baseZ,
        rotSpeed,
        currentZ: baseZ,
        style: {}
      });
    }
  }

  private updatePositions() {
    const scrollY = window.scrollY || window.pageYOffset || 0;
    const loopSpan = 1150;

    this.particles.forEach((p, i) => {
      let z = p.baseZ + scrollY * 0.75;
      let shiftCount = Math.floor((z - (-700)) / loopSpan);
      let currentZ = z - (shiftCount * loopSpan);
      if (currentZ > 450) currentZ -= loopSpan;
      if (currentZ < -700) currentZ += loopSpan;

      const normZ = (currentZ - (-700)) / 1150;
      let opacity = 0;
      if (normZ < 0.15) opacity = normZ / 0.15;
      else if (normZ > 0.82) opacity = (1 - normZ) / 0.18;
      else opacity = 1;

      opacity = Math.max(0, Math.min(0.24, opacity * 0.24));
      const rot = (scrollY * p.rotSpeed + i * 35) % 360;

      p.style = {
        left: p.baseX + '%',
        top: p.baseY + '%',
        transform: `translate3d(0, 0, ${currentZ}px) rotate(${rot}deg)`,
        opacity: opacity
      };
    });
  }
}
