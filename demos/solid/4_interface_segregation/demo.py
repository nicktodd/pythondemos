# Interface Segregation Principle (ISP)
# Clients should not be forced to depend on interfaces they don't use

from abc import ABC, abstractmethod

# BAD: Fat interface forces classes to implement methods they don't need
class BadWorker(ABC):
    """One large interface for all worker types"""
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass


class BadHumanWorker(BadWorker):
    """Human workers can do everything"""
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating lunch...")
    
    def sleep(self):
        print("Human sleeping...")


class BadRobotWorker(BadWorker):
    """Robots don't eat or sleep - but they're forced to implement these methods!"""
    def work(self):
        print("Robot working...")
    
    def eat(self):
        # Robots don't eat! But we're forced to implement this
        raise NotImplementedError("Robots don't eat!")
    
    def sleep(self):
        # Robots don't sleep! But we're forced to implement this
        raise NotImplementedError("Robots don't sleep!")


# GOOD: Small, focused interfaces
class Workable(ABC):
    """Interface for things that can work"""
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    """Interface for things that can eat"""
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    """Interface for things that can sleep"""
    @abstractmethod
    def sleep(self):
        pass


class HumanWorker(Workable, Eatable, Sleepable):
    """Humans implement all three interfaces"""
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating lunch...")
    
    def sleep(self):
        print("Human sleeping...")


class RobotWorker(Workable):
    """Robots only implement Workable - that's all they need!"""
    def work(self):
        print("Robot working...")


class SuperRobot(Workable, Sleepable):
    """Advanced robots that can work and enter sleep mode"""
    def work(self):
        print("Super robot working...")
    
    def sleep(self):
        print("Super robot entering sleep mode...")


# Manager classes
class BadWorkManager:
    """Forces all workers to have eat() and sleep()"""
    def manage_worker(self, worker: BadWorker):
        worker.work()
        worker.eat()   # Will fail for robots!
        worker.sleep() # Will fail for robots!


class WorkManager:
    """Only requires work() method"""
    def manage_work(self, worker: Workable):
        worker.work()


class BreakManager:
    """Manages breaks - only for workers that eat and sleep"""
    def manage_break(self, worker: Eatable):
        if isinstance(worker, Eatable):
            worker.eat()
        if isinstance(worker, Sleepable):
            worker.sleep()


# Usage
if __name__ == "__main__":
    print("=== Bad Example - Fat Interface ===")
    human = BadHumanWorker()
    robot = BadRobotWorker()
    
    bad_manager = BadWorkManager()
    
    print("Managing human:")
    bad_manager.manage_worker(human)
    
    print("\nManaging robot (will crash!):")
    try:
        bad_manager.manage_worker(robot)
    except NotImplementedError as e:
        print(f"ERROR: {e}")
    
    print("\n=== Good Example - Segregated Interfaces ===")
    human2 = HumanWorker()
    robot2 = RobotWorker()
    super_robot = SuperRobot()
    
    work_manager = WorkManager()
    break_manager = BreakManager()
    
    print("All workers can work:")
    work_manager.manage_work(human2)
    work_manager.manage_work(robot2)
    work_manager.manage_work(super_robot)
    
    print("\nOnly humans take eating breaks:")
    break_manager.manage_break(human2)
    
    print("\nRobots don't need breaks - no error!")
    print("Super robots can sleep:")
    super_robot.sleep()
