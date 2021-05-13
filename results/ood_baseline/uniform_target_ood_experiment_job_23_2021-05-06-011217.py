store = {}
store['timestamp']=1620259937
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=23']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=23
store['worker_id']=23
store['num_workers']=40
store['config']={'seed': 26, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.161097764968872})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.5259101390838623})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5367178916931152})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.6449456214904785})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6884, 'crossentropy': 1.976848046875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 42135], ['id', 42236], ['ood', 47975], ['ood', 51835], ['id', 53446]], 'labels': [2, 4, 0, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8257986307144165})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.0215182304382324})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1738035678863525})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.336540699005127})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6775, 'crossentropy': 1.667011328125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 2150], ['ood', 18641], ['ood', 17014], ['id', 13182], ['id', 54051]], 'labels': [1, 4, 7, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5605952739715576})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6785465478897095})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.012803077697754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.261430263519287})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6782, 'crossentropy': 1.46964931640625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 39315], ['id', 34802], ['id', 45012], ['ood', 27544], ['ood', 20573]], 'labels': [7, 3, 5, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.8951349258422852})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.1803722381591797})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.2704172134399414})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.576690196990967})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6345, 'crossentropy': 1.55354716796875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 10760], ['ood', 34056], ['ood', 50033], ['ood', 23445], ['id', 31979]], 'labels': [3, 6, 9, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.696674108505249})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.1964011192321777})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.4213199615478516})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.4657416343688965})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6293, 'crossentropy': 1.6339037109375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 17619], ['id', 47341], ['ood', 56917], ['id', 29701], ['id', 51358]], 'labels': [6, 9, 6, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3613176345825195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.6947262287139893})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8054280281066895})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.001373291015625})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7019, 'crossentropy': 1.2643939453125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 8237], ['ood', 28302], ['ood', 45593], ['id', 48530], ['id', 13094]], 'labels': [2, 7, 4, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3338510990142822})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6157605648040771})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7459115982055664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8808192014694214})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6961, 'crossentropy': 1.23520341796875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 24371], ['id', 46909], ['id', 7996], ['ood', 9975], ['ood', 11569]], 'labels': [0, 9, 1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3586606979370117})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3584556579589844})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7344369888305664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5956394672393799})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.6652040481567383})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7383, 'crossentropy': 1.223069921875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 48507], ['ood', 19457], ['ood', 36858], ['ood', 3997], ['ood', 25045]], 'labels': [6, 2, 9, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1320385932922363})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.11579167842865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3810017108917236})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4193270206451416})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.40913987159729})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7688, 'crossentropy': 1.09836318359375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 6756], ['ood', 34456], ['ood', 39584], ['id', 30208], ['id', 42825]], 'labels': [9, 6, 0, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.216465711593628})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3217475414276123})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5933701992034912})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.379836916923523})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7464, 'crossentropy': 1.0664048828125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 13801], ['ood', 5580], ['id', 4125], ['ood', 16502], ['ood', 51674]], 'labels': [1, 3, 4, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1953802108764648})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3703510761260986})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4052456617355347})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4041831493377686})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7439, 'crossentropy': 1.068467578125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 53713], ['ood', 30798], ['id', 40134], ['ood', 17570], ['ood', 49755]], 'labels': [4, 7, 8, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2254018783569336})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.371049404144287})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4705883264541626})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4006938934326172})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7306, 'crossentropy': 1.100095703125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 26948], ['id', 57743], ['id', 15586], ['ood', 6048], ['ood', 53618]], 'labels': [8, 5, 7, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9876322746276855})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0470843315124512})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0241278409957886})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2287330627441406})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8003, 'crossentropy': 0.9001833984375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 56212], ['id', 23243], ['ood', 15754], ['id', 38798], ['ood', 26226]], 'labels': [9, 8, 8, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9824865460395813})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9609857797622681})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9022799134254456})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1463329792022705})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0717259645462036})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2010209560394287})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8359, 'crossentropy': 0.83025849609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 27056], ['ood', 38563], ['id', 41060], ['ood', 28], ['id', 28172]], 'labels': [6, 0, 6, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0590704679489136})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0335352420806885})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0345497131347656})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0626343488693237})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2398083209991455})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8096, 'crossentropy': 0.91365126953125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 6292], ['id', 26993], ['ood', 26263], ['id', 48907], ['id', 56076]], 'labels': [7, 1, 0, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0106308460235596})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9881114959716797})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0047181844711304})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0445092916488647})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1130650043487549})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8219, 'crossentropy': 0.86797509765625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 58145], ['ood', 49493], ['ood', 16409], ['id', 47161], ['id', 33769]], 'labels': [5, 9, 3, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.064152479171753})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9684557914733887})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0667117834091187})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1233253479003906})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.125531554222107})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 0.8788951171875}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 52664], ['id', 43456], ['ood', 49822], ['ood', 27092], ['id', 36348]], 'labels': [3, 3, 9, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.061565637588501})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9710091948509216})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9991536140441895})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9821515083312988})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0623385906219482})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8098, 'crossentropy': 0.8824603515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28096], ['ood', 40711], ['ood', 13803], ['id', 31941], ['id', 36833]], 'labels': [4, 6, 6, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0243926048278809})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0245606899261475})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0403287410736084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.994465708732605})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9595541954040527})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1276071071624756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1361815929412842})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0915753841400146})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 0.8410021484375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 28285], ['id', 16102], ['ood', 6190], ['id', 46357], ['id', 14831]], 'labels': [2, 6, 1, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8988980054855347})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9393422603607178})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.041966438293457})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.959751307964325})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8308, 'crossentropy': 0.8757279296875}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 46183], ['id', 42795], ['ood', 59678], ['id', 4394], ['id', 50839]], 'labels': [9, 0, 9, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9511909484863281})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9261541366577148})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9910455346107483})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9932885766029358})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1619243621826172})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 0.8599978515625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49890], ['ood', 41244], ['id', 40030], ['ood', 7025], ['id', 38630]], 'labels': [5, 5, 4, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9608964920043945})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8597252368927002})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9064784049987793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9248818159103394})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.914684534072876})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8457, 'crossentropy': 0.769726318359375}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 51436], ['ood', 52413], ['id', 27056], ['id', 50332], ['ood', 3050]], 'labels': [4, 8, 4, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9136940836906433})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7906063199043274})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9091523289680481})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8069601058959961})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9436672329902649})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8504, 'crossentropy': 0.719838134765625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 51463], ['id', 48716], ['ood', 41447], ['ood', 22250], ['id', 47506]], 'labels': [3, 0, 0, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.053912878036499})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9066191911697388})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9804689288139343})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0389142036437988})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1621018648147583})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8325, 'crossentropy': 0.81543984375}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 20463], ['ood', 2172], ['ood', 8383], ['id', 54472], ['ood', 3377]], 'labels': [1, 2, 1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0423212051391602})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8754279613494873})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9414229393005371})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9374790191650391})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9990978837013245})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8443, 'crossentropy': 0.749702001953125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 39129], ['id', 43453], ['ood', 14291], ['id', 53262], ['ood', 42814]], 'labels': [0, 9, 5, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9720160365104675})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8828661441802979})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7907178401947021})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8799377679824829})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9251760840415955})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8985135555267334})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8637, 'crossentropy': 0.6921951171875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 18602], ['ood', 27365], ['ood', 37145], ['ood', 22980], ['ood', 760]], 'labels': [9, 5, 5, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8717304468154907})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7973964810371399})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7957548499107361})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7295310497283936})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.792569637298584})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.793267548084259})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9006065130233765})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8855, 'crossentropy': 0.6370833984375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 28442], ['id', 56344], ['ood', 35112], ['ood', 54871], ['ood', 37270]], 'labels': [8, 5, 2, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9672486782073975})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8090073466300964})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7976315021514893})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8398990631103516})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9249873161315918})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1319987773895264})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.659412841796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 31331], ['id', 45050], ['ood', 3589], ['id', 16701], ['id', 13805]], 'labels': [4, 8, 6, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9491360187530518})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8824736475944519})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7724653482437134})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8703019618988037})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9354904294013977})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9306084513664246})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8695, 'crossentropy': 0.678811572265625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8439], ['id', 1213], ['id', 24042], ['ood', 11628], ['id', 51687]], 'labels': [9, 2, 3, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8814289569854736})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6983736753463745})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7809014320373535})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7126502990722656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8257216215133667})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.644493505859375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 56614], ['id', 42891], ['id', 8009], ['id', 59093], ['ood', 4805]], 'labels': [2, 2, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9578691720962524})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7391970157623291})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7112154960632324})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7222650647163391})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7638877630233765})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8278147578239441})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8987, 'crossentropy': 0.56522275390625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 44580], ['id', 53392], ['id', 8857], ['id', 10895], ['ood', 19013]], 'labels': [3, 7, 4, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9307900667190552})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7167462110519409})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.71955806016922})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.783905565738678})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8884230852127075})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8811, 'crossentropy': 0.63467109375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 27935], ['ood', 44947], ['ood', 59061], ['ood', 23928], ['ood', 671]], 'labels': [2, 0, 6, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.915184736251831})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7316040992736816})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7319846153259277})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7022086381912231})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8214269876480103})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7764452695846558})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7693712711334229})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8981, 'crossentropy': 0.580797998046875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 25533], ['id', 5822], ['id', 49115], ['ood', 37486], ['id', 16313]], 'labels': [2, 4, 2, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9513183832168579})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7696894407272339})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7623965740203857})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7495088577270508})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7501108646392822})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7440029382705688})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8177660703659058})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9186519384384155})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7372393012046814})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8492889404296875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8018014430999756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7483323812484741})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.659517333984375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 11323], ['ood', 56959], ['ood', 12121], ['ood', 56215], ['id', 44938]], 'labels': [5, 5, 1, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.958687424659729})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7479583024978638})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7492790818214417})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7352433800697327})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7168413400650024})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8019704818725586})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.803009033203125})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6987478137016296})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7196090817451477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8535667061805725})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7566291093826294})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.60383642578125}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 38876], ['id', 5181], ['ood', 31897], ['id', 28923], ['ood', 18220]], 'labels': [6, 7, 5, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9823224544525146})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7165477275848389})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6775370836257935})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7053638696670532})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.705172598361969})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.74930739402771})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.598701806640625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 53678], ['id', 21937], ['id', 40036], ['ood', 13276], ['ood', 13227]], 'labels': [0, 7, 6, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9583954811096191})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7441713213920593})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7207521200180054})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7166333198547363})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6527938842773438})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7672321796417236})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9109876155853271})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7083410024642944})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.551966259765625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 6494], ['id', 37249], ['ood', 48744], ['ood', 28027], ['id', 24514]], 'labels': [2, 5, 1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9413799047470093})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6702806353569031})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7128325700759888})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7223331928253174})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7428845167160034})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8839, 'crossentropy': 0.61150966796875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 50838], ['id', 36162], ['ood', 18020], ['id', 6551], ['id', 55688]], 'labels': [1, 9, 9, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9197211265563965})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7911743521690369})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7213741540908813})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6699929237365723})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7119724154472351})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7309567928314209})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7763403654098511})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.57134501953125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 22454], ['id', 15355], ['id', 17949], ['id', 52427], ['id', 26994]], 'labels': [7, 8, 4, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9122089147567749})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.667698860168457})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6554098129272461})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5927085876464844})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.752265214920044})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7129566073417664})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6787569522857666})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9007, 'crossentropy': 0.53833232421875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 10519], ['id', 25786], ['ood', 12803], ['id', 20306], ['ood', 50526]], 'labels': [1, 1, 6, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.871224045753479})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.639580249786377})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.674045205116272})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6747568845748901})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8229351043701172})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8842, 'crossentropy': 0.62677646484375}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 22583], ['ood', 28992], ['id', 30765], ['id', 13584], ['ood', 7626]], 'labels': [0, 8, 4, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8671121597290039})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7135423421859741})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6259401440620422})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7138897180557251})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7352170348167419})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6955211162567139})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.52778095703125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 40570], ['id', 35105], ['ood', 37416], ['id', 15328], ['id', 41880]], 'labels': [8, 9, 1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9732054471969604})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7359181642532349})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7182314395904541})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.638471245765686})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6406160593032837})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7932565212249756})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6446239948272705})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.558850634765625}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 2946], ['ood', 44648], ['ood', 11666], ['ood', 46567], ['id', 59015]], 'labels': [8, 0, 7, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9071137309074402})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5952096581459045})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6422444581985474})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.676623523235321})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7801249027252197})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.587197900390625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 517], ['ood', 35670], ['id', 35247], ['ood', 7686], ['ood', 19139]], 'labels': [1, 5, 5, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9099358916282654})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6586076021194458})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.685560405254364})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6654646396636963})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6878269910812378})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.602699365234375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 56032], ['id', 42280], ['id', 16631], ['ood', 49232], ['id', 4719]], 'labels': [2, 2, 8, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.946317195892334})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7023006081581116})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6260428428649902})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7552350759506226})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.799835205078125})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7473759651184082})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.544068994140625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 46420], ['ood', 2479], ['ood', 23994], ['ood', 58585], ['id', 29332]], 'labels': [6, 0, 1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9424838423728943})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7331817746162415})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6881585121154785})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6665667295455933})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6732010841369629})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7896270155906677})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8088507056236267})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8991, 'crossentropy': 0.560291162109375}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 39060], ['ood', 22379], ['ood', 36657], ['ood', 8596], ['id', 12110]], 'labels': [0, 8, 8, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9127058982849121})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6789835691452026})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6653221845626831})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.649273693561554})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7380199432373047})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7372795343399048})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7953498363494873})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.552162158203125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 45668], ['id', 40499], ['ood', 17682], ['ood', 33200], ['id', 52711]], 'labels': [7, 9, 4, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9639177322387695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.706789493560791})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5875157117843628})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6462103128433228})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6807534694671631})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7175673246383667})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.526231787109375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 51964], ['ood', 59199], ['ood', 41186], ['ood', 58869], ['ood', 50260]], 'labels': [6, 9, 9, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.938139796257019})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6697292327880859})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7405318021774292})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6591289043426514})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7484526634216309})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.712900698184967})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7953555583953857})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.6057724609375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 26270], ['id', 42021], ['id', 46083], ['ood', 27201], ['ood', 41456]], 'labels': [3, 6, 2, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.949600100517273})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6562761068344116})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.706436276435852})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7167075872421265})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6794002056121826})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.57082177734375}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 56657], ['ood', 22925], ['id', 55134], ['ood', 53626], ['id', 39017]], 'labels': [7, 3, 6, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8121457099914551})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6580194234848022})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6807913780212402})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6771212816238403})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6520535945892334})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6917306780815125})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6781835556030273})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7351067066192627})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.566374609375}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 56640], ['id', 50376], ['ood', 54175], ['ood', 34637], ['id', 49584]], 'labels': [0, 7, 2, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.896765410900116})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6585757732391357})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6025499701499939})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6733170747756958})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6873811483383179})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6544617414474487})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.52789873046875}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 57113], ['ood', 46872], ['id', 26398], ['id', 54744], ['ood', 39601]], 'labels': [2, 0, 5, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8320651054382324})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6818113327026367})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6020504236221313})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6260429620742798})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6975358128547668})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6242001056671143})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.56192041015625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 15264], ['ood', 1226], ['ood', 19905], ['ood', 11418], ['id', 53091]], 'labels': [1, 3, 9, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8473764657974243})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6475801467895508})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5968831777572632})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6531358957290649})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6701740622520447})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6241246461868286})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.533638916015625}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 28458], ['ood', 58551], ['ood', 13482], ['ood', 24212], ['ood', 21776]], 'labels': [3, 9, 7, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9196150302886963})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6524224281311035})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5664143562316895})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.610307514667511})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5832785367965698})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6573288440704346})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.512898486328125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 51967], ['ood', 24456], ['id', 11854], ['id', 35875], ['id', 43359]], 'labels': [7, 9, 7, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8163118362426758})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6073626279830933})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6541856527328491})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6309084296226501})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6508409380912781})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.56485908203125}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 19256], ['id', 16046], ['ood', 9023], ['ood', 38879], ['ood', 58634]], 'labels': [3, 2, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8396613597869873})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7591612339019775})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6312962770462036})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6227492094039917})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5605579614639282})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6517411470413208})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.629000186920166})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6417189836502075})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.51608779296875}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 29688], ['ood', 38307], ['id', 23122], ['ood', 31330], ['id', 55007]], 'labels': [5, 3, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9571967124938965})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6490798592567444})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5730166435241699})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6642330288887024})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6597518920898438})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6057555675506592})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.529036279296875}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 20349], ['id', 34221], ['id', 25661], ['id', 11030], ['id', 8853]], 'labels': [0, 4, 8, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8882877826690674})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6313203573226929})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5810869932174683})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6564857363700867})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5810405015945435})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6537689566612244})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6091816425323486})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6037768125534058})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.548901708984375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 6394], ['id', 58151], ['id', 40887], ['id', 55637], ['id', 3056]], 'labels': [0, 4, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8855736255645752})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6188231706619263})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6356186270713806})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6080070734024048})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6041905283927917})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6972970962524414})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6936279535293579})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7070579528808594})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.532345654296875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 43241], ['ood', 32551], ['id', 39508], ['id', 32653], ['id', 19596]], 'labels': [2, 8, 6, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9227432012557983})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6483396291732788})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5846839547157288})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.652868390083313})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6689788103103638})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6170464754104614})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.525225732421875}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 47417], ['ood', 43777], ['id', 27360], ['id', 18864], ['id', 46349]], 'labels': [7, 0, 7, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.860887348651886})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6577030420303345})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6046380996704102})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6538272500038147})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6077499389648438})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5799911022186279})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6769227385520935})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6218873262405396})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7081211805343628})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.52305703125}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 40663], ['ood', 20510], ['id', 11467], ['id', 47213], ['id', 47949]], 'labels': [0, 8, 3, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8203233480453491})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6876785755157471})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.600966215133667})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5566701889038086})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5821322202682495})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6081969738006592})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6366515159606934})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.507479150390625}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 2262], ['ood', 41995], ['id', 9698], ['ood', 5094], ['ood', 8305]], 'labels': [7, 2, 0, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9606311917304993})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6919059753417969})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6382752656936646})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7149059772491455})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6381936073303223})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6488049030303955})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6655566692352295})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6407954692840576})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.5490646484375}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 7367], ['id', 56711], ['id', 43726], ['ood', 36823], ['ood', 38311]], 'labels': [3, 5, 6, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8993364572525024})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6323023438453674})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5512834191322327})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5493286848068237})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5482666492462158})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.599050760269165})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6575642824172974})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6812680959701538})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.500345263671875}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 16456], ['id', 15785], ['ood', 43872], ['id', 26142], ['ood', 6241]], 'labels': [5, 3, 7, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9014377593994141})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6426417827606201})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5771387815475464})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5927302837371826})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5968393087387085})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.554589569568634})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.585414707660675})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5719155073165894})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6023419499397278})
store['active_learning_steps'][66]['training']['best_epoch']=6
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.537060498046875}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 48559], ['ood', 39492], ['id', 36533], ['ood', 57565], ['ood', 34523]], 'labels': [7, 8, 0, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9428086280822754})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6457679867744446})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5932016372680664})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6270552277565002})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6096196174621582})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5828527212142944})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5868781805038452})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5869630575180054})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6119784116744995})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.50463818359375}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 22387], ['id', 14684], ['ood', 6589], ['id', 34662], ['ood', 56325]], 'labels': [4, 7, 3, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8858343958854675})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6888673305511475})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6222121119499207})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6065694093704224})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6295821666717529})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6647549271583557})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6915802359580994})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.536636328125}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 47648], ['ood', 9455], ['ood', 7249], ['ood', 50774], ['ood', 58758]], 'labels': [8, 6, 4, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8531537652015686})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6336183547973633})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.641930878162384})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5978918075561523})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.611465573310852})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6717944145202637})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6215572357177734})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.5782537109375}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 57940], ['id', 14359], ['ood', 24730], ['ood', 35590], ['ood', 15314]], 'labels': [4, 1, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.885198175907135})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6121671795845032})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5827343463897705})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6003533601760864})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6484465599060059})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6364037394523621})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.52930830078125}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 10787], ['id', 36268], ['ood', 42769], ['ood', 3272], ['ood', 58149]], 'labels': [9, 5, 8, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8797098398208618})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6220320463180542})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5646471977233887})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6070674657821655})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6317555904388428})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6088075041770935})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.520698046875}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 42076], ['ood', 14887], ['ood', 51125], ['id', 25348], ['ood', 28065]], 'labels': [8, 9, 4, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.870218813419342})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6178975701332092})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5703756809234619})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5676490068435669})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5911493301391602})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6087774038314819})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.551102340221405})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5943237543106079})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6380812525749207})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6317622065544128})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.455041162109375}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 8481], ['ood', 30765], ['id', 24547], ['id', 38662], ['id', 20089]], 'labels': [6, 1, 4, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9092477560043335})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6248374581336975})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6109714508056641})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.60983806848526})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5407590270042419})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5464001893997192})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5928077697753906})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6134167909622192})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.475748828125}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 7013], ['id', 50504], ['id', 553], ['id', 14663], ['ood', 29836]], 'labels': [9, 2, 1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7868300080299377})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6150362491607666})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5445437431335449})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5789539813995361})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.569671630859375})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5412251949310303})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5748146176338196})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6110687851905823})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5805510878562927})
store['active_learning_steps'][74]['training']['best_epoch']=6
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.46814521484375}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 55455], ['id', 40217], ['ood', 4603], ['ood', 24539], ['ood', 8080]], 'labels': [5, 0, 1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8031529188156128})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6021546125411987})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5300874710083008})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6073079109191895})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5511521697044373})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5910360813140869})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.50827255859375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 30381], ['ood', 25077], ['ood', 43732], ['ood', 44802], ['id', 22853]], 'labels': [6, 2, 0, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8632171154022217})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6054774522781372})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5440168976783752})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5351561307907104})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5575445890426636})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6297786235809326})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5395451784133911})
store['active_learning_steps'][76]['training']['best_epoch']=4
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.47001728515625}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 40730], ['id', 13679], ['id', 26921], ['id', 1277], ['id', 39433]], 'labels': [3, 6, 9, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9898287057876587})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6924149394035339})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5906531810760498})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5724626779556274})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5456311702728271})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5562787055969238})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6160204410552979})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6505680084228516})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.488980029296875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 49076], ['id', 41924], ['ood', 34976], ['ood', 918], ['ood', 45288]], 'labels': [1, 9, 4, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8778671026229858})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6957891583442688})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6264402866363525})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5548369288444519})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5656167268753052})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.684139609336853})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.652600884437561})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.484930908203125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 48578], ['id', 56649], ['ood', 52904], ['id', 23341], ['id', 15505]], 'labels': [3, 9, 8, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8943142890930176})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6684693098068237})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6434931755065918})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5842550992965698})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5971091985702515})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6398928165435791})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6013159155845642})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.50099990234375}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 51963], ['id', 8054], ['ood', 7544], ['ood', 14826], ['id', 38899]], 'labels': [5, 3, 9, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7746683359146118})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5853649377822876})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5257583856582642})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5282012224197388})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5855081081390381})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5672990679740906})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.500371875}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 50052], ['id', 47370], ['id', 15527], ['id', 43742], ['id', 19391]], 'labels': [0, 0, 6, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8884464502334595})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6077315807342529})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5175521373748779})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5729751586914062})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6305084228515625})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6425962448120117})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.488469580078125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 17060], ['id', 35019], ['ood', 31368], ['ood', 17143], ['ood', 52280]], 'labels': [8, 9, 7, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9052144289016724})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6079779863357544})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5608516931533813})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5891891717910767})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5560606718063354})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.605108380317688})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.611534833908081})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.637385904788971})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.5138580078125}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 736], ['id', 39733], ['ood', 33706], ['id', 53201], ['id', 53345]], 'labels': [8, 9, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8575836420059204})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6047361493110657})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6600102186203003})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5571150779724121})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5523744821548462})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6134779453277588})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5691636800765991})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5610116720199585})
store['active_learning_steps'][83]['training']['best_epoch']=5
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.49991376953125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 33227], ['id', 35096], ['id', 10913], ['id', 10289], ['ood', 57472]], 'labels': [6, 8, 6, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8179831504821777})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6319547295570374})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5792765617370605})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5692919492721558})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5151246786117554})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5484309792518616})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5339398980140686})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5845456123352051})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.4872966796875}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 26871], ['ood', 8709], ['id', 38915], ['ood', 50242], ['id', 2910]], 'labels': [8, 6, 6, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8612794876098633})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6295259594917297})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5803075432777405})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5637170076370239})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6257725358009338})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5784270167350769})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.635654091835022})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.528192578125}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 41057], ['ood', 1895], ['ood', 21420], ['id', 59209], ['id', 51036]], 'labels': [8, 0, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8617628216743469})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6010549068450928})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5542617440223694})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5531355738639832})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5898797512054443})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5951715707778931})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5705099701881409})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.451317529296875}
