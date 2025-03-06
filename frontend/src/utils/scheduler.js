/**
 * Task scheduling utility for background operations
 */

import { REMOTE_CONFIG_KEYS } from './browserDetection';

/**
 * Simple task scheduler for handling async operations
 */
class Scheduler {
  constructor() {
    this.tasks = [];
    this.isRunning = false;
    this.config = {
      maxConcurrent: 2,
      retryLimit: 3,
      retryDelay: 1000
    };
  }

  /**
   * Add a task to the scheduler
   * @param {Function} taskFn - Function to execute
   * @param {Object} options - Task options
   * @returns {Promise} Task result promise
   */
  scheduleTask(taskFn, options = {}) {
    return new Promise((resolve, reject) => {
      this.tasks.push({
        fn: taskFn,
        options,
        resolve,
        reject,
        attempts: 0
      });
      
      this.runTasks();
    });
  }

  /**
   * Run pending tasks
   */
  async runTasks() {
    if (this.isRunning) return;
    
    this.isRunning = true;
    
    while (this.tasks.length > 0) {
      const task = this.tasks.shift();
      
      try {
        const result = await task.fn();
        task.resolve(result);
      } catch (error) {
        console.error('Task error:', error);
        
        if (task.attempts < this.config.retryLimit) {
          // Retry the task
          task.attempts++;
          this.tasks.push(task);
          await new Promise(r => setTimeout(r, this.config.retryDelay));
        } else {
          task.reject(error);
        }
      }
    }
    
    this.isRunning = false;
  }
}

// Create and export a singleton instance
const scheduler = new Scheduler();

export default scheduler;
