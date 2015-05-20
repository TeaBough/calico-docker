import unittest
from sh import docker


class TestDiags(unittest.TestCase):
    def test_diags(self):
        """
        Test that the diags command successfully uploads the diags file.
        """
        docker_exec = docker.bake("exec")
        host1_exec = docker_exec.bake("-t", "host1", "bash", "-c")
        link = host1_exec("/code/dist/calicoctl diags")
        assert "https://transfer.sh/" in link
