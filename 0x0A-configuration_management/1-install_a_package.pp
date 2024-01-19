# Instalar un paquete

package { 'puppet-lint':
  ensure   => '2.5.0',
  name     => 'puppet-lint',
  provider => 'gem',
  source   => 'http://rubygems.org',
}
