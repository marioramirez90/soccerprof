import { Component, OnInit, OnDestroy, HostListener, inject, PLATFORM_ID } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';

interface Particle {
  sphereX: number;
  sphereY: number;
  sphereZ: number;
  explodedX: number;
  explodedY: number;
  baseZ: number;
  rotSpeed: number;
  targetSize: number;
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
  private platformId = inject(PLATFORM_ID);
  particles: Particle[] = [];
  private animFrameId: number | null = null;
  private timeAngle = 0;

  ngOnInit() {
    this.initParticles();
    if (isPlatformBrowser(this.platformId)) {
      this.startAnimationLoop();
    }
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
    const total = 24;
    this.particles = [];
    const sphereRadius = 150;

    for (let i = 0; i < total; i++) {
      const y = 1 - (i / (total - 1)) * 2;
      const radiusAtY = Math.sqrt(Math.max(0, 1 - y * y));
      const phi = i * 2.3999632;

      const sphereX = Math.cos(phi) * radiusAtY * sphereRadius;
      const sphereY = y * sphereRadius * 0.75;
      const sphereZ = Math.sin(phi) * radiusAtY * sphereRadius;

      const explodedX = 6 + (i % 6) * 17 + (Math.random() * 6 - 3);
      const explodedY = 8 + Math.floor(i / 6) * 23 + (Math.random() * 8 - 4);
      const baseZ = -750 + (i * 60);
      const rotSpeed = 0.2 + Math.random() * 0.35;
      const targetSize = 64 + (i % 4) * 16;

      this.particles.push({
        sphereX,
        sphereY,
        sphereZ,
        explodedX,
        explodedY,
        baseZ,
        rotSpeed,
        targetSize,
        style: {}
      });
    }
  }

  private startAnimationLoop() {
    const loop = () => {
      this.timeAngle += 0.4;
      this.updatePositions();
      this.animFrameId = requestAnimationFrame(loop);
    };
    this.animFrameId = requestAnimationFrame(loop);
  }

  private updatePositions() {
    const scrollY = typeof window !== 'undefined' ? (window.scrollY || window.pageYOffset || 0) : 0;
    
    // Explosion progress: 0 at top (sphere), 1 fully exploded after 220px scroll
    const rawProgress = Math.min(1, Math.max(0, scrollY / 220));
    const burst = 1 - Math.pow(1 - rawProgress, 3);

    const centerPercentX = 50;
    const centerPercentY = 40;
    const loopSpan = 1200;

    this.particles.forEach((p, i) => {
      const radY = ((this.timeAngle + i * 8) * Math.PI) / 180;
      const cosY = Math.cos(radY);
      const sinY = Math.sin(radY);

      const rotX = p.sphereX * cosY - p.sphereZ * sinY;
      const rotZ = p.sphereX * sinY + p.sphereZ * cosY;
      const rotY = p.sphereY;

      let zExp = p.baseZ + scrollY * 0.85;
      let shiftCount = Math.floor((zExp - (-750)) / loopSpan);
      let currentZExp = zExp - (shiftCount * loopSpan);
      if (currentZExp > 450) currentZExp -= loopSpan;
      if (currentZExp < -750) currentZExp += loopSpan;

      const winW = typeof window !== 'undefined' ? window.innerWidth : 1440;
      const winH = typeof window !== 'undefined' ? window.innerHeight : 900;

      const spherePercentX = centerPercentX + (rotX / winW) * 100;
      const spherePercentY = centerPercentY + (rotY / winH) * 100;

      const currentX = spherePercentX * (1 - burst) + p.explodedX * burst;
      const currentY = spherePercentY * (1 - burst) + p.explodedY * burst;
      const currentZ = rotZ * (1 - burst) + currentZExp * burst;

      const currentSize = 50 * (1 - burst) + p.targetSize * burst;

      let opacity = 0.26 * (1 - burst);
      if (burst > 0) {
        const normZ = (currentZExp - (-750)) / 1200;
        let scrollOp = 1;
        if (normZ < 0.15) scrollOp = normZ / 0.15;
        else if (normZ > 0.82) scrollOp = (1 - normZ) / 0.18;
        opacity += Math.max(0, Math.min(0.24, scrollOp * 0.24)) * burst;
      }

      const rotAngle = (this.timeAngle * 0.5 + scrollY * p.rotSpeed + i * 25) % 360;

      p.style = {
        left: `${currentX}%`,
        top: `${currentY}%`,
        width: `${Math.round(currentSize)}px`,
        height: `${Math.round(currentSize)}px`,
        transform: `translate3d(-50%, -50%, ${Math.round(currentZ)}px) rotate(${Math.round(rotAngle)}deg)`,
        opacity: Math.max(0.04, Math.min(0.28, opacity))
      };
    });
  }
}
