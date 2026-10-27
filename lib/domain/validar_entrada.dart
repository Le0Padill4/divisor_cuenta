import 'cuenta.dart';

class ValidarEntrada {
  static const double _propinaMaximaPermitida = 100;

  String? validar(Cuenta cuenta) {
    if (!cuenta.monto.isFinite) {
      return 'Monto inválido';
    }
    if (cuenta.personas < 1) {
      return 'Debe haber al menos una persona';
    }
    if (!cuenta.porcentajePropina.isFinite) {
      return 'Propina inválida';
    }
    if (cuenta.porcentajePropina > _propinaMaximaPermitida) {
      return 'La propina no puede superar el 100%';
    }
    return null;
  }
}
